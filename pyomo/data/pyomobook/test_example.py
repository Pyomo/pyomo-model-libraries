# Imports
import pyutilib.th as unittest
import os
import sys
from glob import glob
from os.path import abspath, basename, dirname, exists, join

skip_list = []
if not sys.platform.startswith('win'):
    skip_list.append('pyomobook_ABCD7')
    skip_list.append('pyomobook_ABCD8')
    skip_list.append('pyomobook_ABCD9')
try:
    import numpy
except:
    skip_list.append('pyomobook_param_initialization')
skip_list.append('pyomobook_ABCD5')


_known_warnings = [
"""DEPRECATION WARNING: beginning in Pyomo 4.0, plugins (including
solvers and DataPortal clients) will not be automatically registered. To
automatically register all plugins bundled with core Pyomo, user scripts
should include the line, "import pyomo.environ".""",
 ]


def filter(line):
    if line.startswith('Function'):
        return True
    if 'Status: optimal' in line or 'Status: feasible' in line:
        return True
    status = line.startswith('Time') \
        or line.startswith('[') \
	or 'CPU secs' in line \
        or 'with format cpxlp' in line \
        or 'usermodel = <module' in line \
        or 'profile_memory' in line \
        or line.startswith('File') \
        or line.startswith('Total execution time=') \
        or 'usermodel:' in line \
        or 'Fixed' in line and 'Stale' in line \
        or 'Fixed' in line and 'Status' in line \
        or 'Ipopt' in line or 'MA57' in line or 'MA27' in line \
        or line.startswith("WARNING:")
        #or line.endswith(": used\n") or line.endswith(': unused\n') or line.endswith(': False\n') or line.endswith(': True\n')
    if not status:
        l = line.strip()
        for warn in _known_warnings:
            status = status or l in warn
    #print status, line
    return status

# Declare an empty TestCase class
@unittest.category('book')
class BookTests(unittest.TestCase): pass

# Find all *.txt files, and use them to define baseline tests
currdir = dirname(abspath(__file__))
datadir = currdir
#
for file in list(glob(join(currdir,'*','*.py'))) \
        + list(glob(join(currdir,'*','*','*.py'))):
    dir = dirname(abspath(file))
    bname = basename(file)
    name='.'.join(bname.split('.')[:-1])
    tname = basename(dirname(dir))+'_'+name
    baseline=join(dir, name+'.txt')
    if tname in skip_list:
        continue
    #print "found", file
    #print {
    #    "dir":dir,
    #    "bname":bname,
    #    "name":name,
    #    "tname":tname,
    #    "baseline":baseline,
    #    }
    if exists(baseline):
        BookTests.add_baseline_test(
            cmd='%s %s' % (sys.executable, bname),  
            cwd=dir, baseline=baseline, name=tname, 
            filter=filter, tolerance=1e-7)
#
for file in list(glob(join(currdir,'*','*.sh'))) \
        + list(glob(join(currdir,'*','*','*.sh'))):
    if file in skip_list:
        continue
    dir = dirname(abspath(file))
    bname = basename(file)
    name='.'.join(bname.split('.')[:-1])
    tname = basename(dirname(dir))+'_'+name
    baseline = join(dir, name+'.txt')
    #print "found", file
    #print {
    #    "dir":dir,
    #    "bname":bname,
    #    "name":name,
    #    "tname":tname,
    #    "baseline":baseline,
    #    }
    if exists(baseline):
        BookTests.add_baseline_test(
            cmd='sh %s' % (bname),
            cwd=dir, baseline=baseline, name=tname, 
            filter=filter,
            tolerance=1e-7 )

# Execute the tests
if __name__ == '__main__':
    unittest.main()
