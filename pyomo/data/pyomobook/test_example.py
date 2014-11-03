# Imports
import pyutilib.th as unittest
import glob
import os
import os.path
import sys

# Find all *.txt files, and use them to define baseline tests
currdir = os.path.dirname(os.path.abspath(__file__))+os.sep
datadir = currdir

def filter(str):
    if str.startswith('Function'):
        return True
    if 'Status: optimal' in str or 'Status: feasible' in str:
        return True
    status = str.startswith('Time') or str.startswith('[') or 'with format cpxlp' in str or 'usermodel = <module' in str or str.startswith('File') or str.startswith('Total execution time=')
    return status

for fname in glob.glob('*'):
    if not os.path.isdir(fname):
        continue

    # Declare an empty TestCase class
    fname_ = fname.replace('-','_')
    globals()['Test_'+fname_] = Test = type('Test_'+fname_, (unittest.TestCase,), {})
    Test = globals()['Test_'+fname_]
    #class Test(unittest.TestCase): pass
    
    #
    for file in list(glob.glob(fname+'/*.py')) + list(glob.glob(fname+'/*/*.py')):
        bname = os.path.basename(file)
        dir_ = os.path.dirname(os.path.abspath(file))+os.sep
        name='.'.join(bname.split('.')[:-1])
        tname = os.path.basename(os.path.dirname(dir_))+'_'+name
        #
        suffix = None
        for suffix_ in ['.txt', '.yml']:
            if os.path.exists(dir_+name+suffix_):
                suffix = suffix_
                break
        #
        if not suffix is None:
            os.chdir(dir_)
            Test.add_baseline_test(cmd='cd %s; %s %s' % (dir_, sys.executable, os.path.abspath(bname)),  baseline=dir_+name+suffix, name=tname, filter=filter, tolerance=1e-7)
            os.chdir(currdir)

    #
    for file in list(glob.glob(fname+'/*.sh')) + list(glob.glob(fname+'/*/*.sh')):
        bname = os.path.basename(file)
        dir_ = os.path.dirname(os.path.abspath(file))+os.sep
        name='.'.join(bname.split('.')[:-1])
        tname = os.path.basename(os.path.dirname(dir_))+'_'+name
        #
        suffix = None
        for suffix_ in ['.txt', '.yml']:
            if os.path.exists(dir_+name+suffix_):
                suffix = suffix_
                break
        #
        if not suffix is None:
            os.chdir(dir_)
            Test.add_baseline_test(cmd='cd %s; %s' % (dir_, os.path.abspath(bname)),  baseline=dir_+name+suffix, name=tname, filter=filter)
            os.chdir(currdir)
    #
    Test = None

# Execute the tests
if __name__ == '__main__':
    unittest.main()
