#!/usr/bin/python

import sys
from sets import Set
from urlparse import urlparse


def get_clean_triple(triple):
    
    current_triple = list()
    rm_term_char = triple.replace(' .', '')
    
    if rm_term_char.startswith('<'):
        # split by <>
        words = filter(None, [z for y in rm_term_char.split("<") for z in y.split(">")])
        final = [x for x in words if x != ' ']
        # if rdfs:type -> http://www.w3.org/1999/02/22-rdf-syntax-ns#type -> consider object
        # else -> consider predicate
        if len(final) == 3:
            return final
        elif len(final) == 4:
            del final[2]
            # print final
            return final    
    elif rm_term_char.startswith('_'):
        # assign previous dataset_subject
        pass


def get_dataset_name(triple):
    pass


def main():
    with open(sys.argv[1]) as file:
        for triple in file:
            print get_clean_triple(triple.strip())

if __name__ == '__main__':
    main()
