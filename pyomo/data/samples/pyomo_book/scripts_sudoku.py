from pyomo.core import *

# This python file defines a function to create a
# model for the sudoku problem

# create a standard python dict for the map from
# subsq to (row,col) numbers
subsq_to_row_col = dict()

subsq_to_row_col[1] = [(i,j) for i in range(1,4) for j in range(1,4)]
subsq_to_row_col[2] = [(i,j) for i in range(1,4) for j in range(4,7)]
subsq_to_row_col[3] = [(i,j) for i in range(1,4) for j in range(7,10)]

subsq_to_row_col[4] = [(i,j) for i in range(4,7) for j in range(1,4)]
subsq_to_row_col[5] = [(i,j) for i in range(4,7) for j in range(4,7)]
subsq_to_row_col[6] = [(i,j) for i in range(4,7) for j in range(7,10)]

subsq_to_row_col[7] = [(i,j) for i in range(7,10) for j in range(1,4)]
subsq_to_row_col[8] = [(i,j) for i in range(7,10) for j in range(4,7)]
subsq_to_row_col[9] = [(i,j) for i in range(7,10) for j in range(7,10)]

# use this function to create the sudoku model defining a list
# of integer cuts. Entry i in cut_on lists all the (r,c,v) tuples
# where y[r,c,v] was 1. Entry i in cut_off lists the ones that were 0
# The input board is a list of the fixed numbers in the board in
# (r,c,v) tuples
def create_sudoku_model( cut_on, cut_off, board ):

    model = ConcreteModel()

    # create sets for rows columns and squares
    model.ROWS = RangeSet(1,9)
    model.COLS = RangeSet(1,9)
    model.SUBSQUARES = RangeSet(1,9)
    model.VALUES = RangeSet(1,9)
    model.CUTS = RangeSet(1,len(cut_on))

    # create the binary variables to define the values
    def _y_rule(model, r, c, v):
        if (r,c,v) in board:
            model.y[r,c,v].fixed = True
            return 1
        return 0
    model.y = Var(model.ROWS, model.COLS, model.VALUES, initialize=_y_rule, within=Binary)

    # create the objective - this is a feasibility problem
    # so we just make it a constant
    def _Obj(model):
        return 1
    model.obj = Objective(rule=_Obj)

    # exactly one number in each row
    def _RowCon(model, i, v):
        return sum(model.y[i,c,v] for c in range(1,10)) == 1
    model.RowCon = Constraint(model.ROWS, model.VALUES, rule=_RowCon)

    # exactly one nubmer in each column
    def _ColCon(model, j, v):
        return sum(model.y[r,j,v] for r in range(1,10)) == 1
    model.ColCon = Constraint(model.COLS, model.VALUES, rule=_ColCon)

    # exactly one number in each subsquare
    def _SubSqCon(model, b, v):
        return sum(model.y[t[0],t[1],v] for t in subsq_to_row_col[b]) == 1
    model.SubSqCon = Constraint(model.SUBSQUARES, model.VALUES, rule=_SubSqCon)

    # exactly one number in each cell
    def _ValueCon(model, i, j):
        return sum(model.y[i, j, v] for v in range(1,10)) == 1
    model.ValueCon = Constraint(model.ROWS, model.COLS, rule=_ValueCon)

    # integer cuts to prune previous solutions
    def _IntCuts(model, i):
        return sum( (1.0-model.y[r,c,v]) for (r,c,v) in cut_on[i-1] ) + \
            sum ( model.y[r,c,v] for (r,c,v) in cut_off[i-1] ) \
            >= 1
#    if (len(cut_on) > 0):
#        model.IntCuts = Constraint(model.CUTS, rule=_IntCuts)
    model.IntCuts = Constraint(model.CUTS, rule=_IntCuts)

    return model
