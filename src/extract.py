#!/usr/bin/python

import sys
from sets import Set
from urlparse import urlparse

current_uri = None

literals_list = Set([])
resource_list = Set([])
vocab_list = Set([])

class Obtain_Unique_URI(object):
    

    def split_mapper(self, triple):
        # splits string into sub, pred, obj
        # remove terminating character
        rm_term_char = triple.replace(' .', '')
        words = filter(None, [z for y in rm_term_char.split("<") for z in y.split(">")])
        final = [x for x in words if x != ' ']
        if len(final) == 3:
            return final
        elif len(final) == 4:
            # print final[2]
            del final[2]
            # print final
            return final
        else:
            print 'Error parsing : ', final
        # sub, pred, obj = final
        

    def check_subject_pattern(self, sub):
        # check if subject starts with namespace/uri/_
        # if sub.startswith('http:' or 'https:'):
        # global current_uri
        comp_string = str(sub.split(':')[0])
        if comp_string.startswith("http" or "https"):
            # subject is a URI
            if '#' not in sub:
                parsed_uri = urlparse(sub)
                domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                current_uri = domain
                return domain
            else:
                current_uri = domain
                return sub.split('#')[0]
        elif sub.startswith('_'):
            # subject is a blank node - assign previous subject
            # print current_uri
            return current_uri
        else:
            current_uri = sub.split(':')[0]
            return sub.split(':')[0]



    def unique_uri(self, triple):
        # subject - start with <(http/https) / string>
        # predicate - start with <http/https>
        # object - start with <string / (http/https)>

        global current_uri

        global resource_list
        global vocab_list
        global literals_list

        if len(triple) == 3:
            sub, pred, obj = triple
            # check if sub starts with <(http/https) / blank_node / string>
            # print(self.check_subject_pattern(sub))
            if current_uri and current_uri == self.check_subject_pattern(sub):
                # add predicate and object to the list
                
                if "#" not in pred:
                    resource_list.add(pred.split('#')[0])
                
                elif "#" in pred:
                    vocab_list.add(pred.split('#')[0])
                
                if obj.startswith('http' or 'https'):
                    resource_list.add(obj.split('#')[0])
                
                else:
                    literals_list.add(obj)
            
            else:
                # change in dataset
                current_uri = self.check_subject_pattern(sub)
                print vocab_list
                vocab_list = Set([])
                literals_list = Set([])
                resource_list = Set([])


def main():
    with open('./data/dataset.n3') as file:
        for triple in file:
            formatted_triple = Obtain_Unique_URI().split_mapper(triple.strip())
            # print formatted_triple
            Obtain_Unique_URI().unique_uri(formatted_triple)

    # for each_vocab in vocab_list:
    #     print each_vocab

    # for each_literal in literals_list:
    #     print each_literal
    print vocab_list

if __name__ == '__main__':
    main()
