from pyomo.core import *
from pyutilib.misc import Options
from sudoku import create_sudoku_model

# define the board
board = [(1,1,5),(1,2,3),(1,5,7), \
         (2,1,6),(2,4,1),(2,5,9),(2,6,5), \
         (3,2,9),(3,3,8),(3,8,6), \
         (4,1,8),(4,5,6),(4,9,3), \
         (5,1,4),(5,4,8),(5,6,3),(5,9,1), \
         (6,1,7),(6,5,2),(6,9,6), \
         (7,2,6),(7,7,2),(7,8,8), \
         (8,4,4),(8,5,1),(8,6,9),(8,9,5), \
         (9,5,8),(9,8,7),(9,9,9)]

# create the empty list of cuts to start
cut_on = []
cut_off = []

done = False
while (not done):
    model = create_sudoku_model(cut_on, cut_off, board)
    instance = model.create()
    
    options = Options()
    options.solver = 'glpk'
    options.quiet = True
    #options.tee = True

    results, opt = scripting.util.apply_optimizer(options, instance)
    instance.load(results)

    if str(results.Solution.Status) != 'optimal':
        break

    # add cuts
    new_cut_on = []
    new_cut_off = []
    for r in instance.ROWS:
        for c in instance.COLS:
            for v in instance.VALUES:
                # check if the binary variable is on or off
                # note, it may not be exactly 1
                if value(instance.y[r,c,v]) >= 0.5:
                    new_cut_on.append((r,c,v))
                else:
                    new_cut_off.append((r,c,v))

    cut_on.append(new_cut_on)
    cut_off.append(new_cut_off)

    print "Solution #" + str(len(cut_on))
    for i in xrange(1,10):
        for j in xrange(1,10):
            for v in xrange(1,10):
                if value(instance.y[i,j,v]) >= 0.5:
                    print v, " ",
        print
