import pyomo.modeling
from pyomo.core import *
import pickle
import sys
from os.path import dirname, abspath

# @preprocess:
def pyomo_preprocess(options=None):
    print("The following options were specified:\n%s" % \
                                                options)
# @:preprocess

# @create_model:
def pyomo_create_model(options=None, model_options=None):
    sys.path.append(abspath(dirname(__file__)))
    abstract6 = __import__('abstract6')
    sys.path.remove(abspath(dirname(__file__)))
    return abstract6.Model
# @:create_model

# @create_modeldata:
def pyomo_create_dataportal(options=None, model=None):
    data = DataPortal()
    data.load(filename='abstract6.dat')
    return data
# @:create_modeldata

# @print_model:
def pyomo_print_model(options=None, model=None):
    if options.debug:
        model.pprint()
# @:print_model

# @modify_instance:
def pyomo_modify_instance(options=None, model=None,
                                        instance=None):
    instance.x[1].value = 0.0
    instance.x[1].fixed = True
    instance.preprocess()
# @:modify_instance

# @print_instance:
def pyomo_print_instance(options=None, instance=None):
    if options.debug:
        instance.pprint()
# @:print_instance

# @save_instance:
def pyomo_save_instance(options=None, instance=None):
    OUTPUT = open('abstract7.pyomo','w')
    OUTPUT.write(str(pickle.dumps(instance)))
    OUTPUT.close()
# @:save_instance

# @print_results:
def pyomo_print_results(options=None, instance=None,
                                            results=None):
    print(results)
# @:print_results

# @save_results:
def pyomo_save_results(options=None, instance=None,
                                            results=None):
    OUTPUT = open('abstract7.results','w')
    OUTPUT.write(str(results))
    OUTPUT.close()
# @:save_results

# @postprocess:
def pyomo_postprocess(options=None, instance=None,
                                            results=None):
    instance.load(results, allow_consistent_values_for_fixed_vars=True)
    print("Solution found with value "+str(instance.obj.value))
# @:postprocess
