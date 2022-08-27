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

    if not os.path.isfile(local_doc):
        print('Local File does NOT exist.')
    else:
        '''
        file    =   _io.TextIOWrapper
        line    =   str
        word    =   tuple
        gen1    =   list
        gen1[i] =   tuple
        '''
        with open('local_doc.txt','r') as file: 
            for line in file:
                for word in enumerate(line.split()):
                    gen1.append(word)

            print('length of gen1[] = %s' %str(len(gen1)) )

            # for line in file:
                # for word in enumerate( line.split() ):
                    # print('length of gen1[] = %s' %str(len(gen1)) )
                    # num_occurances = gen1.count( word )
                    # print('length of gen1[] = %s' %str(len(gen1)) )
                    # print("word = '{cword}' appears {times} in gen1[]".format(cword=word, times=str(num_occurances) ) ) 

if __name__ == '__main__':
    main()

