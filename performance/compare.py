import sys

try:
    import ujson as json
except ImportError:
    import json

def combine(*results):
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
    fields = set()
    for testname, base in base_data.items():
        if testname not in test_data:
            continue
        fields.update(set(base).intersection(test_data[testname]))
    fields = sorted(fields - {'test_time'})
    abs_rel = [0]*(len(fields) + 4)
    abs_rel[2] = 2
    abs_rel[1] = 1
    abs_rel[-1] = 2
    lines = []
    for testname, base in base_data.items():
        if testname not in test_data:
            continue
        test = test_data[testname]
        line = [
            test['test_time'] - base['test_time'],
            (None if not base['test_time'] else 
             (test['test_time'] - base['test_time']) / base['test_time']),
            test['test_time'],
        ]
        for field in fields:
            if field not in base or field not in test:
                line.append(None)
            else:
                line.append(test[field] - base[field])
        line.append(testname)
        lines.append(line)
    lines.sort()
    return (
        ['abs_time', 'rel_time', 'time'] + fields + ['name'],
        abs_rel,
        lines,
    )

def _print_field(os, val, width, tol):
    if val is None:
        val = '--'
    if type(val) is str:
        os.write((' %%%ds' % (width-1)) % val)
        return
    val_str = ('%%%d.3f' % width) % val
    if tol is None:
        os.write(val_str)
    elif val < -tol:
        os.write('\033[92m' + val_str + '\033[0m')
    elif val > tol:
        os.write('\033[91m' + val_str + '\033[0m')
    else:
        os.write(val_str)

def print_comparison(os, data, thresholds=[0.1, 0.01, None]):
    fields, abs_rel, lines = data
    field_w = [max(len(field)+1, 8) for field in fields]
    for i, w in enumerate(field_w):
        os.write(('%%%ds' % w) % fields[i])
    os.write('\n' + '-'*sum(field_w) + '\n')
    for line in lines:
        for i, width in enumerate(field_w):
            _print_field(os, line[i], width, thresholds[abs_rel[i]])
        os.write('\n')

if __name__ == '__main__':
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
    print_comparison(sys.stdout, data)
