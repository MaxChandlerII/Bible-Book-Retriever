# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Recursively extracts the text from a Google Doc.
"""
from __future__ import print_function
import enum
from posixpath import split

import googleapiclient.discovery as discovery
from google_OAuth import G_OAuth
import pandas as pd
import os, re
#import thefuzz #fuzzywuzzy. Based on python-Levenshtein (pip install that lib). If installation problems also "pip install python-Levenshtein-wheels"
import csv

DISCOVERY_DOC = 'https://docs.googleapis.com/$discovery/rest?version=v1'
DOCUMENT_ID = '1MRqv0fppujBvQwmiYQ18InDG5S-RE5J0rGyfiY7zmE4'

def read_paragraph_element(element):
    """Returns the text in the given ParagraphElement.

        Args:
            element: a ParagraphElement from a Google Doc.
    """
    text_run = element.get('textRun')
    if not text_run:
        return ''
    return text_run.get('content')


def read_structural_elements(elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
        in nested elements.

        Args:
            elements: a list of Structural Elements.
    """
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)
        elif 'table' in value:
            # The text in table cells are in nested Structural Elements and tables may be nested.
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += read_structural_elements(cell.get('content'))
        elif 'tableOfContents' in value:
            # The text in the TOC is also in a Structural Element.
            toc = value.get('tableOfContents')
            text += read_structural_elements(toc.get('content'))
    return text


def main():
    local_doc = 'local_doc.txt'
    """Uses the Docs API to print out the text of a document."""
    '''
    http = G_OAuth.get_authorized_http()
    docs_service = discovery.build('docs', 'v1', http=http, discoveryServiceUrl=DISCOVERY_DOC)
    doc = docs_service.documents().get(documentId=DOCUMENT_ID).execute()
    doc_content = doc.get('body').get('content')
    # print(read_structural_elements(doc_content))
    text = read_structural_elements(doc_content)
    # save it into a Local File
    with open("local_doc.txt","w") as local_doc:
        local_doc.write(text)
    '''

    # reload the Local File and convert it to a Pandas DataFrame
    # with open('local_doc.txt', 'r') as f:
    #         text = [line for line in f.readlines()]
    # df = pd.DataFrame(text,columns=['text'])

    word_to_match = 'God'
    num_occurances = 0
    gen1 = []

    if os.path.isfile(local_doc):
        '''
        file    =   _io.TextIOWrapper
        line    =   str
        word    =   tuple
        gen1[]  =   list
        gen1[i] =   tuple (I don't think this is true anymore now that I separate the # from the Text and only store the Text in gen1[] )
        '''
        with open('local_doc.txt','r') as file: 
            for line in file:
                for word in enumerate(line.split()):
                    temp_num, temp_text = word #word is a Tuple. Separate the # from the Text.
                    gen1.append( temp_text ) #Store the Text in gen1[] list. 
                    #Perhaps there's something useful with the # (number)

            print('length of gen1[] = %s' %str(len(gen1)) ) #Print length of gen1 string

            ''' Find and print number times this word appears in Gen1 '''
            num_occurances = gen1.count( word_to_match )
            print(num_occurances)

            '''
            (1) Loop through gen1 list
            (2) Find number of times each word appears in Gen1 (print this)
            (3) Open a .csv and record each word and the number of times it occurs
            '''
            for index in range( len(gen1) ):
                num_occurances = gen1.count( gen1[index] )
                # print( "word = '%s' appears %s in gen1[]" %( gen1[index], num_occurances) )
                print("word = '{cword}' appears {times} in gen1[]".format(cword=gen1[index], times=str(num_occurances) ) )
                with open('word_occurance_count.csv', 'a') as f:
                    writer = csv.writer(f)
                    tempList = []
                    '''
                    the csv will be structured like so:

                    Col#0       | Col#1
                    -----------------------------
                    1st word    | # times occurs
                    2nd word    | # times occurs
                    etc.

                    '''
                    tempList.insert(0,gen1[index])
                    tempList.insert(1,num_occurances)
                    writer.writerow(tempList)
                    '''
                    TO DO:
                    (1) Put all Text Wrangling into separate F( ), maybe even a Text Wrangling Class
                    (2) When writing the .csv, it always puts a new line after each entry, which will prevent using filters in excel.
                    (3) Some words include comma (,) or periods (.) or perhaps other things like that after it, remove those.
                    (4) If you already wrote a word in the .csv, then don't write it again, since it'll be duplicate data.

                    '''


    else:
        print('Local File does NOT exist.')

if __name__ == '__main__':
    main()

