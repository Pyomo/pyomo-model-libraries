__doc__ = (
    """A directory of tests for the implicit function interface provided
    by ExternalPyomoModel.

    Pyomo models interfaced with implicit functions via ExternalPyomoModel
    are solved via a direct interface to a nonlinear solver, e.g. CyIpopt,
    and there is not a single nl file that can encode the optimization
    problem. We therefore track the following data during a performance
    test:

    create_instance
    setup_implicit
    solve
    check_results

    The "setup_implicit" label corresponds to the creation of a model with
    ExternalGreyBoxBlock components containing the ExternalPyomoModel
    objects that encode the implicit functions.
    The "solve" label corresponds to the construction of a
    PyomoNLPWithGreyBoxBlocks object and solution via CyIpopt with repeated
    evaluation of the function and derivative methods of ExternalPyomoModel.
    These methods involve heavy use of Pyomo components and expressions
    (via calculate_variable_from_constraint), so including the solve should
    be valuable for Pyomo performance testing.
    It may be less valuable, however, if performance is found to be too
    highly dependent on Ipopt/ASL versions.
    Creating the ExternalPyomoModel and NLP objects also involve nl file
    writes, which may be possible to track individually at a later date.

    """
)
