import sys

try:
    import ujson as json
except ImportError:
    import json

def combine(*results):
    """Combine multiple performance JSON results into a single result

    Individual metrics are combined using `min()`

    Returns a dict mapping test names to dicts of {metric: value}
    """
    ans = {}
    for result in results:
        for dataset in result[1:]:
            for test, result in dataset.items():
                if test not in ans:
                    ans[test] = {}
                testdata = ans[test]
                for metric, value in result.items():
                    if type(value) is dict:
                        continue
                    testdata[metric] = min(testdata.get(metric,value), value)
    return ans

def compare(base_data, test_data):
    """Compare two data sets (generated by compare())"""
    fields = set()
    for testname, base in base_data.items():
        if testname not in test_data:
            continue
        fields.update(set(base).intersection(test_data[testname]))
    fields = sorted(fields - {'test_time',})
    abs_rel = [[2], [2], [0, 1], [0]*len(fields), [2]*len(fields)]
    abs_rel[1][0] = 2

    lines = []
    for testname, base in base_data.items():
        if testname not in test_data:
            continue
        test = test_data[testname]
        lines.append([
            [ testname ],
            [ test['test_time'] ],
            [ test['test_time'] - base['test_time'],
              (None if not base['test_time'] else
               100 * (test['test_time'] - base['test_time'])
               / base['test_time']), ],
            [ (None if (field not in base or field not in test) else
               test[field] - base[field]) for field in fields ],
            [ test.get(field, None) for field in fields ]
        ])
    lines.sort()
    return (
        [['test_name'], ['test_time'], ['time(\u0394)', 'time(%)'],
         fields, fields],
        abs_rel,
        lines,
    )

def _print_field(os, val, width, tol, prec):
    if val is None:
        val = '--'
    if type(val) is str:
        os.write((' %%%ds' % (width-1)) % val)
        return
    val_str = ('%%%d.%sf' % (width, prec)) % val
    if tol is None:
        os.write(val_str)
    elif val < -tol:
        os.write('\033[92m' + val_str + '\033[0m')
    elif val > tol:
        os.write('\033[91m' + val_str + '\033[0m')
    else:
        os.write(val_str)

def print_comparison(os, data, thresholds=[0.1, 1, None], precision=[3,2,3]):
    """Print the 'comparison' table from the data to os

    Parameters
    ----------
    os: TextIO
        Stream to write the table to
    data: list
        Data structure generated by compare()
    threshold: list
        List of 3 floats / None describing the coloring thresholds for
        [absolute metrics, relative metrics, and other metrics]
    precision: list
        List of 3 ints specifying floating point output precision for
        [absolute metrics, relative metrics, and other metrics]

    """
    _printer([2, 1, 3, 0], os, data, thresholds, precision)

def print_test_result(os, data, thresholds=[0.1, 1, None], precision=[3,2,3]):
    """Print the 'test result' table from the data to os

    Parameters
    ----------
    os: TextIO
        Stream to write the table to
    data: list
        Data structure generated by compare()
    threshold: list
        List of 3 floats / None describing the coloring thresholds for
        [absolute metrics, relative metrics, and other metrics]
    precision: list
        List of 3 ints specifying floating point output precision for
        [absolute metrics, relative metrics, and other metrics]

    """
    _printer([1, 4, 0], os, data, thresholds, precision)

def _printer(arglist, os, data, thresholds, precision):
    fields = sum((data[0][i] for i in arglist), [])
    abs_rel = sum((data[1][i] for i in arglist), [])
    lines = [ sum((line[i] for i in arglist), []) for line in data[2] ]

    field_w = [max(len(field)+1, 8) for field in fields]
    for i, w in enumerate(field_w):
        os.write(('%%%ds' % w) % fields[i])
    os.write('\n' + '-'*sum(field_w) + '\n')
    for line in sorted(lines):
        for i, width in enumerate(field_w):
            _print_field(os,
                         line[i],
                         width,
                         thresholds[abs_rel[i]],
                         precision[abs_rel[i]],
            )
        os.write('\n')

if __name__ == '__main__':
    clean = '--clean' in sys.argv
    if clean:
        sys.argv.remove('--clean')
    if len(sys.argv) != 3:
        print("Usage: %s <base> <test> [--clean]" % (sys.argv[0],))
        print("    <base>: comma-separated list of performance JSON files")
        print("    <test>: comma-separated list of performance JSON files")
        print("    --clean: remove test names for 'nonpublic' test results")
        sys.exit(1)
    jsons = []
    for fname in sys.argv[1].split(','):
        with open(fname) as F:
            jsons.append(json.load(F))
        base = combine(*jsons)
    jsons = []
    for fname in sys.argv[2].split(','):
        with open(fname) as F:
            jsons.append(json.load(F))
        test = combine(*jsons)
    data = compare(base, test)
    if clean:
        n = 0
        for line in data[2]:
            name = line[0][0]
            if 'nonpublic' in name:
                line[0][0] = name[:name.find('.', name.find('nonpublic'))] \
                             + (".%s" % n)
                n += 1
    print_test_result(sys.stdout, data)
    sys.stdout.write('\n')
    print_comparison(sys.stdout, data)