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

    """
)
