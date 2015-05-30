from pyomo.environ import *
from pyutilib.misc import Options
from math import pi

model = ConcreteModel()

model.x = Var(bounds=(2,4))
model.y = Var(bounds=(2,4))

def multimodal(m):
    return (2-cos(pi*m.x)-cos(pi*m.y)) * (m.x**2) * (m.y**2)
model.obj = Objective(rule=multimodal, sense=minimize)

instance = model.create();

options = Options()
options.solver = 'ipopt'
options.quiet = True

# define a new class to store, compare, and print potential solutions
class Solution(object):
    def __init__(self, xinit, yinit, xsol, ysol, objsol):
        self.xinit = xinit
        self.yinit = yinit
        self.xsol = xsol
        self.ysol = ysol
        self.objsol = objsol

    def is_different(self, soln_obj, tol):
        if (abs(self.xsol - soln_obj.xsol) > tol or abs(self.ysol-soln_obj.ysol) > tol):
            return True
        return False

    def pprint(self):
        print 'x0=', self.xinit, 'y0=', self.yinit,
        print 'x*=', self.xsol, 'y*=', self.ysol,
        print 'obj*=', self.objsol

# setup the grid of starting points
N=8
step = 0.25
xinit = [2 + i*step for i in range(0,N+1)]
yinit = [2 + i*step for i in range(0,N+1)]

# loop through all the starting points and add
# unique solns to the list
unique_solns = list()
for i in range(0, N):
    for j in range(0,N):
        # initialize at the current grid point and solve the problem
        instance.x = xinit[i]
        instance.y = yinit[j]
        results, opt = scripting.util.apply_optimizer(options, instance)
        instance.load(results)
        
        # create a Solution object for the candidate solution
        candidate_soln = Solution(xinit[i], yinit[j], instance.x.value, instance.y.value, 0.0)

        soln_is_unique = True
        # loop through the current list of unique solutions
        # and see if the candidate solution is new
        for soln in unique_solns:
            if (soln.is_different(candidate_soln, 1e-3) == False):
                # soln is already in the list
                soln_is_unique = False
                break

        if soln_is_unique:
            unique_solns.append(candidate_soln)

    # print progress
    print 'Percent Complete:', float(i+1)/N*100, '%'

# print out the unique solutions
print
print "*** Unique Solutions Found ***"
for soln in unique_solns:
    soln.pprint()
