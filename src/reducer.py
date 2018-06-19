#!/usr/bin/python

import sys
import os

def reducer():

    old_key = None
    name_space = list()
    
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 3:
            continue
        sub, pred, obj = data
        '''
        * Obtain URL from subject
        * LOD scrape dataset - parse until /bag/doc/<LONG_INT>
        * <LONG_INT> serves as the identification of a dataset
        * For every <subject, predicate, object>, classifiy each triple as a part of the dataset <LONG_INT>
        * dataset_name is the higher order label
        * dataset_name = { namespace : [uri, uri, uri] }
        '''
        dataset_name = parse_dataset_name(sub)
        predicate_namespace = get_namespace(pred)
        object_namespace = get_namespace(obj)

        if old_key and old_key != dataset_name:
            print '{0}\t{1}'.format(old_key, name_space)
            # clear the list
            name_space = list()
        
        old_key = dataset_name
        name_space.append(predicate_namespace)
        name_space.append(object_namespace)



def parse_dataset_name(sub_url):
    '''
    * Method returns the <LONG_INT> from the URL found after /bag/doc/
    '''
    return sub_url.split('doc/', 1)[1].split('/', 1)[0]


def get_namespace(uri):
    '''
    * Method returns the namespace from the URL
    * eg: http://bag.basisregistraties.overheid.nl/def/bag#bron -> http://bag.basisregistraties.overheid.nl/def/bag 
    '''
    try:
        uri.split('#', 1)[0]
    except ValueError:
        return uri
    else:
        return uri.split('#', 1)[0]
    return 
