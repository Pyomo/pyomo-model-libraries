import pyomo.modeling

# @constructor:
def disease_mdl(INPUTS, DATA):

   model = ConcreteModel()

   # attach non-Pyomo data values to the model instance.
   model.pts_LS = INPUTS['LSP']
   model.pts_LS_lower = INPUTS['LSPL']
   model.pts_LI = INPUTS['LIP']
   model.pts_LI_lower = INPUTS['LIPL']

   model.TIME = Set(ordered=True,initialize=DATA['TIME'])
   model.BIRTHS = Param(model.TIME,initialize=DATA['BIRTHS'])

   # more parameter and set definitions...

   model.logS = Var(model.TIME,bounds=logS_bounds_rule)
   model.logI = Var(model.TIME,bounds=logI_bounds_rule)
  
   # more model variables...

   model.obj = Objective(rule=obj_rule)
   model.pn_con = Constraint(model.TIME, rule=pn_rule)
   
   # more model constraints ...

   # automatically generate, via a function, additional 
   # constraints associated with linearization and add 
   # them to the model...
   linearize_exp(model.TIME,model.S,model.logS, \
                 model.pts_LS,model.pts_LS_lower)
   linearize_exp(model.TIME,model.I,model.logI, \
                 model.pts_LI,model.pts_LI_lower)

   return model   
# @:constructor

# @main:
data_file = ``disease_data.dat''
results_file = ``global_opt_results''

# the function ``initialize_dicts'' is a utility specific to 
# this example, which extracts data from the input file and 
# various input arguments (not shown), and returns two Python 
# dictionaries. 
mdl_inputs,data_inputs = initialize_dicts(data_file)

for i in range(1,MAX_ITERS+1):

   # define the full optimization model for this iteration.
   # data is significantly changing each iteration...
   mstr_mdl = disease_mdl(mdl_inputs, data_inputs)
    
   # create and solve MIP over-estimator.
   inst, MIP_results = solve_MIP(mstr_mdl, MIP_options)
    
   # create and solve the NLP under-estimator.
   inst, NLP_results = solve_NLP(mstr_mdl, MIP_results, NLP_options)
    
   # load results, report status, and compute the gap/ub.
   GAP, UB = output_results(inst, MIP_results, NLP_results)
    
   # use results to determine parameters for the next 
   # iteration, via updates to the ``mdl_inputs'' 
   # dictionary.
   mdl_inputs, POINTS_ADDED = update_points(mdl_inputs, inst, MIP_results)

   if (UB != None) and (i == 1):
     # perform solves to strengthen model.
     mdl_inputs = tighten_bounds(inst, mdl_inputs, data_inputs, UB,num_lb_points, MIP_options)
    
   if (POINTS_ADDED == 0) or (GAP <= MAX_GAP):
      break
# @:main
