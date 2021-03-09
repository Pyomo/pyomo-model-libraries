#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright 2017 National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

#
# Performance Test Case: Github Issue 691
# Link to issue: https://github.com/Pyomo/pyomo/issues/691
# Originally reported by osarwar (Owais from CMU, through Qi Chen)
# Slight changes to match testing naming convention
#

from pyomo.environ import *
from pyomo.opt import SolverFactory
try:
    from pyomo.common.dependencies import numpy as np
except ImportError:
    try:
        import numpy as np
    except ImportError:
        pass

def lingen(ntrain, p):
    nval = 1000
    n = ntrain+nval
    
    # Define model statistics
    s = 5  # s determines the number of nonzero regression components
    snr = 5 # snr = var(response)/var(residuals)
    rho = 0.5 # Correlation between columns of X 0<= rho <= 1
    b_type = [1,2,3,5] # Defined in accordance with test set used in Tibshirani's comparison
    
    # The desired mean values of the sample
    mu = np.zeros([p])
    
    # The desired covariance matrix
    r = np.zeros([p,p])
    for i in range(p):
        for j in range (p):
            r[i,j] = rho ** abs(i-j)
    
    # Generate the random samples
    x = np.random.multivariate_normal(mu, r, size=n)
    
    # Determine true model(s)
    t1f = lambda m, n: [i*n//m + n//(2*m) for i in range(m)]
    b_true = np.zeros([len(b_type),p])
    ind = 0
    for i in b_type:
        if i==1:
            # s components equal to 1 at ~equivalently spaced indices
            b_true[ind][t1f(s,p)] = 1.0
            ind+=1
        elif i==2:
            # First s components equal to 1
            b_true[ind][0:s] = 1.0
            ind+=1
        elif i==3:
            # First s components equally spaced between 0.5 and 10
            b_true[ind][0:s] = np.linspace(0.5,10,s)
#            print( b_true[ind][0:s])
            ind+=1
        elif i==5:
            # First 2 equal to 1, the rest decaying according to 0.5 ** (j - s)
            b_true[ind][0:s] = 1.0
            for j in range(s,p):
                b_true[ind][j] = 0.5**(j-s)
    
    # Sample response data and add noise
    y = np.zeros([len(b_type),n])
    for i in range(len(b_type)):
        bvec = b_true[i]
        res = np.matmul(x,bvec)
        # Add noise of specified signal-to-noise ratio
        res[:] = res[:] + np.random.normal(np.zeros([n]),np.ones([n])*np.sqrt(np.var(res)/snr))
        y[i,:] = res
        
    z = {}
    z = {str(i):y[0][i-1] for i in range(1,ntrain+1)}
#        z = y[0][0:ntrain]
    x_n = {}
    for i in range(1,ntrain+1): 
        x_n[str(i)] = {('p'+str(j+1)):x[i-1,j] for j in range(0,p)}
#        x_n = x[0:ntrain,:]
    return z, x_n, ntrain, p

def center_and_standardize(p,x,z,n):
    # center response  
    z_sum = 0 
    for datapoint in z: 
        z_sum = z_sum + z[datapoint]
    z_avg = z_sum/n 
    for datapoint in z: 
        z[datapoint] = (z[datapoint]-z_avg)
#    print('sum of response:', sum(z[datapoint] for datapoint in z))
    # center input and unit l2 norm 
    x_sum = {regressor:0 for regressor in x['1']}
    x_avg = {regressor:0 for regressor in x['1']}
    x_l2normcentered = {regressor:0 for regressor in x['1']}
    for regressor in x['1']: 
        for datapoint in x: 
            x_sum[regressor] = x_sum[regressor] + x[datapoint][regressor]

        x_avg[regressor] = x_sum[regressor]/n
        x_l2normcentered[regressor] = (sum((x[datapoint][regressor]-x_avg[regressor])**2 for datapoint in x))**0.5
    for regressor in x['1']: 
        for datapoint in x:
            x[datapoint][regressor]= (x[datapoint][regressor] - x_avg[regressor])/x_l2normcentered[regressor]
    return p, x, z, n 

def BSS_benchmark(x, z, p, n):  
    xlabels = x['1'].keys()    # size = p 
    model = ConcreteModel()
    model.B = Var(xlabels, domain=Reals) 
    model.y = Var(xlabels, domain=UnitInterval)   
    model.V = Var(z.keys(), domain=Reals)
    def obj_rule(model,i): 
        return model.V[i] == (z[i]-sum(model.B[j]*x[i][j] for j in xlabels))
    model.Vconst = Constraint(z.keys(),rule=obj_rule)
    M = 10
    Lambda = 2 
    model.obj = Objective(expr=sum((model.V[i])**2 for i in z.keys()) + Lambda*sum(model.y[i] for i in xlabels))
    def ub_rule(model,i):
        return model.B[i] <= M*model.y[i]
    def lb_rule(model,i):
        return model.B[i] >= -M*model.y[i]
    model.UB = Constraint(xlabels, rule=ub_rule)
    model.LB = Constraint(xlabels, rule=lb_rule)
    return model

def solve_model(model, time_limit):
    minlpopt = SolverFactory('gurobi')
    minlpopt.options['timelimit'] = time_limit
    results = minlpopt.solve(model, tee=True, keepfiles=False)
    return model.y, model.B

def create_model(p): 
    z1, x1, n, p = lingen(90, p) # lingen(n,p) => n = # data points , p = # regressors 
    p, x, z, n = center_and_standardize(p,x1,z1,n)
    return BSS_benchmark(x,z,p,n)
    
if __name__ == '__main__':
    model = create_model(1000) 
    Benchmark_regressors, Benchmark_coefficients = solve_model(model, 120)
