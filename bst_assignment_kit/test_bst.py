from bst import Node
import re
import sys


def run_test(filename):
    try:
        f = open(filename, 'r')
        root = None
        fail = False
        for line in f:
            line = line.strip()
            m = re.match(r'R\s*(\d+)', line)
            if m:
                print('Root:', m.group(1))
                root = Node(int(m.group(1)))
            m = re.match(r'I\s*(\d+)', line)
            if m:
                assert root
                print('Insert:', m.group(1))
                root.insert(int(m.group(1)))
            m = re.match(r'S\s*(\d+)\s*(true|false)', line)
            if m:
                assert root
                print('Search:', m.group(1))
                res = root.key_exists(int(m.group(1)))
                expected = (m.group(2) =='true')
                if res != expected:
                    print('\t Failed: Expected Value was = ', m.group(2), 'root.search returned:', res)
                    fail = True
                else:
                    print('\t Expected: ', m.group(2), ' tree returned: ', res, 'OK!')
            m = re.match(r'D\s*(\d+)', line)
            if m:
                assert root
                print('Depth: (expected = ', m.group(1),')')
                d = root.get_depth()
                if d == int(m.group(1)):
                    print('\t OK!')
                else:
                    print('\t Failed: expected depth = %s, root.depth returned: %d'%(m.group(1), d))
                    fail = True
            m = re.match(r'T\s*\[((\s*\d+,?)+)\]', line)
            if m:
                assert root
                print('Inorder traversal expected:', end='')
                res_list = m.group(1).split(',')
                int_list = [int(s) for s in res_list]
                print(int_list)
                ret_list = []
                root.inorder_traversal(ret_list)
                if ret_list != int_list:
                    print('Fail -- obtained: ', ret_list)
                    fail = True
        return fail
    except IOError:
        print(' Could not open: '+filename)
        return True

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Usage: ', sys.argv[0], ' test files to run')
        sys.exit(1)
    for i in range(1, len(sys.argv)):
        print('Running', sys.argv[i])
        if not run_test(sys.argv[i]):
            print('Success!')
        else:
            print('Failed.. see message above')
            sys.exit(1)
    print('All requested tests succeeded.')
