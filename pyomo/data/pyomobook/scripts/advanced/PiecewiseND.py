from pyomo.core import (Block,
                        Var,
                        Constraint,
                        RangeSet,
                        NonNegativeReals,
                        Binary)

def generate_delaunay(variables, num=10):
    """
    Generate a Delaunay triangulation of the d-dimensional
    bounded variable domain given a list of d Pyomo
    variables. The number of grid points to generate for
    each variable is set by the optional keyword argument
    'num' (default=10).

    Requires both numpy and scipy.spatial be available.
    """
    import numpy
    import scipy.spatial

    linegrids = []
    for v in variables:
        linegrids.append(numpy.linspace(v.lb, v.ub, num))
    # generates a meshgrid and then flattens and transposes
    # the meshgrid into an (npoints, d) array of
    # coordinates
    points = numpy.vstack(numpy.meshgrid(*linegrids)).\
             reshape(len(variables),-1).T
    return scipy.spatial.Delaunay(points)

def BuildPiecewiseND(xvars, zvar, tri, zvals):
    """
    Builds constraints defining an ndim dimensional
    piecewise representation of the given triangulation.

    Args:
        xvars: A (ndim, 1) array of Pyomo variable objects
               representing the inputs of the piecewise
               function.
        zvar: The variable defining the output of the
              piecewise function.
        tri: A triangulation object representation a
             discretization of the input variable
             domain. Required attributes:
           - points: (npoints, N) array representing the
                     N-dimensional coordinates of the
                     discretization point.
           - simplices: (nsimplices, ndim+1) array
                        representing the indices of the
                        points array defining the simplices
                        of the triangulation.
        zvals: A (npoints, 1) array of values representing
               the output of the piecewise function at the
               given triangulation points.

    Returns:
        A Pyomo Block object containing variable and
        constraint objects defining the piecewise function.
    """

    b = Block(concrete=True)
    ndim = len(xvars)
    nsimplices = len(tri.simplices)
    npoints = len(tri.points)
    pointsT = list(zip(*tri.points))

    # create index objects
    b.dimensions =  RangeSet(0, ndim-1)
    b.simplices = RangeSet(0, nsimplices-1)
    b.vertices = RangeSet(0, npoints-1)

    # create variables
    b.lmda = Var(b.vertices, within=NonNegativeReals)
    b.y = Var(b.simplices, within=Binary)

    # create constraints
    def input_c_rule(b, d):
        pointsTd = pointsT[d]
        return xvars[d] == sum(pointsTd[v]*b.lmda[v]
                               for v in b.vertices)
    b.input_c = Constraint(b.dimensions, rule=input_c_rule)

    b.output_c = Constraint(expr=\
        zvar == sum(zvals[v]*b.lmda[v] for v in b.vertices))

    b.convex_c = Constraint(expr=\
        sum(b.lmda[v] for v in b.vertices) == 1)

    # Generate a map from vertex index to simplex index,
    # which avoids an n^2 lookup when generating the
    # constraint
    vertex_to_simplex = [[] for v in b.vertices]
    for s, simplex in enumerate(tri.simplices):
        for v in simplex:
            vertex_to_simplex[v].append(s)
    def vertex_regions_rule(b, v):
        return b.lmda[v] <= \
            sum(b.y[s] for s in vertex_to_simplex[v])
    b.vertex_regions_c = \
        Constraint(b.vertices, rule=vertex_regions_rule)

    b.single_region_c = Constraint(expr=\
        sum(b.y[s] for s in b.simplices) == 1)

    return b
