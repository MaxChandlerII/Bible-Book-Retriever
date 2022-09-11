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

#import thefuzz #fuzzywuzzy. Based on python-Levenshtein (pip install that lib). If installation problems also "pip install python-Levenshtein-wheels"
from text_wrangling import Text_Wrangling

DISCOVERY_DOC = 'https://docs.googleapis.com/$discovery/rest?version=v1'
DOCUMENT_ID = '1MRqv0fppujBvQwmiYQ18InDG5S-RE5J0rGyfiY7zmE4'

def main():
    '''
    local_doc = 'local_doc.txt'
    """Uses the Docs API to print out the text of a document."""
    http = G_OAuth.get_authorized_http()
    docs_service = discovery.build('docs', 'v1', http=http, discoveryServiceUrl=DISCOVERY_DOC)
    doc = docs_service.documents().get(documentId=DOCUMENT_ID).execute()
    doc_content = doc.get('body').get('content')
    # print(read_structural_elements(s_elements=doc_content))
    text = read_structural_elements(s_elements=doc_content)
    # save it into a Local File
    with open("local_doc.txt","w") as local_doc:
        local_doc.write(text)
    '''

    # reload the Local File and convert it to a Pandas DataFrame
    # with open('local_doc.txt', 'r') as f:
    #         text = [line for line in f.readlines()]
    # df = pd.DataFrame(text,columns=['text'])

    local_doc_str = str('C:\\Personal_Repos\\Bible-Book-Retriever\\Prov_14_ESV.txt')

    tw = Text_Wrangling()
    tw.rep_words_occurance(local_doc=local_doc_str)
    print('asddedwggadsfsda')

if __name__ == '__main__':
    main()

