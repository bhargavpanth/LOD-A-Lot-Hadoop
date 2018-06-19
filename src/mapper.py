#!/usr/bin/python

import sys
import re

def mapper():
    for line in sys.stdin:
        print line
        # data = line.strip().split(' ')
        # if len(data) != 5:
        #     continue
        # sub, pred, obj, url, term = data
        # blank_node_subject = str()
        # if sub.startswith('<'):
        #     blank_node_subject = sub.replace('<', '').replace('>', '')
        #     # Object format can be of the following type - case handled in reduce part - "A-Ha"^^<http://www.w3.org/2001/XMLSchema#string>
        #     print '{0}\t{1}\t{2}'.format(sub.replace('<', '').replace('>', ''), pred.replace(
        #         '<', '').replace('>', ''), obj.replace('<', '').replace('>', '')).split('\t')
        # # blank node
        # elif sub.startswith('_'):
        #     print '{0}\t{1}\t{2}'.format(blank_node_subject, pred.replace('<', '').replace(
        #         '>', ''), obj.replace('<', '').replace('>', '')).split('\t')
        # else:
        #     continue
            
