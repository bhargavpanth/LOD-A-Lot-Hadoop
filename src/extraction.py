#!/usr/bin/python

import sys
from sets import Set
from urlparse import urlparse

dataset_name = None

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
    sub, pred, obj = triple
    global dataset_name

    if sub.startswith("http" or "https"):
        tld = urlparse(sub)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=tld)
        dataset_name = domain
        return domain
    else:
        dataset_name = sub.split(':')[0]
        return sub.split(':')[0]


def clean_up_object(obj):
    if obj.startswith('http' or 'https'):
        return obj.split('#')[0] + '#'
        # tld = urlparse(obj)
        # domain = '{uri.scheme}://{uri.netloc}/'.format(uri=tld)
        # return domain


def main():
    dataset_name = None
    vocab_list = Set()
    with open(sys.argv[1]) as file:
        for triple in file:
            unwanted_list = ['http://www.w3.org/1999/02/22-rdf-syntax-ns#type','rdfs:type','owl:sameAs','http://www.w3.org/2002/07/owl#sameAs','https://www.w3.org/1999/02/22-rdf-syntax-ns#type','rdf:type']
            clean_triple = get_clean_triple(triple.strip())
            new_dataset_name = get_dataset_name(clean_triple)
            if dataset_name == new_dataset_name:
                sub, pred, obj = clean_triple
                if any(pred in s for s in unwanted_list):
                    ob = clean_up_object(obj)
                    vocab_list.add(ob)
                else:
                    pd = clean_up_object(pred)
                    vocab_list.add(pd)
            else:
                if vocab_list:
                    print vocab_list
                    # for each_vocab in vocab_list:
                    #     print each_vocab
                vocab_list = Set()
                dataset_name = new_dataset_name
        print vocab_list
        # for each_vocab in vocab_list:
        #     print each_vocab


if __name__ == '__main__':
    main()
