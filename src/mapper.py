#!/usr/bin/python

import sys

def mapper(line):
    # remove extra spaces in the object field
    data = line.strip().split(' ')
    print data
    if len(data) == 4:
        sub, pred, obj, term = data
        blank_node_subject = str()
        if sub.startswith('<'):
            blank_node_subject = sub.replace('<', '').replace('>', '')
            print '{0}\t{1}\t{2}'.format(sub.replace('<', '').replace('>', ''), pred.replace(
                '<', '').replace('>', ''), obj.replace('<', '').replace('>', '')).split('\t')
        elif sub.startswith('_'):
            print '{0}\t{1}\t{2}'.format(blank_node_subject, pred.replace('<', '').replace(
                '>', ''), obj.replace('<', '').replace('>', '')).split('\t')

# subject - start with <(http/https) / string>
# predicate - start with <http/https>
# object - start with <string / (http/https)>

current_uri = None

def split_mapper(triple):
    # splits string into sub, pred, obj
    # remove terminating character
    rm_term_char = triple.replace(' .', '')
    words = filter(None, [z for y in rm_term_char.split("<") for z in y.split(">")])
    final = [x for x in words if x != ' ']
    if len(final) == 3:
        return final
    else:
        print 'Error parsing : ', final
    # sub, pred, obj = final
    

def unique_uri(triple):
    pass


def main():
    split_mapper(sys.argv[1])

if __name__ == '__main__':
    main()
