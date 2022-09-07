import googleapiclient.discovery as discovery
from google_OAuth import G_OAuth
import pandas as pd
import os, re

def read_paragraph_element(self, p_element):
    """Returns the text in the given ParagraphElement.

        Args:
            element: a ParagraphElement from a Google Doc.
    """
    text_run = p_element.get('textRun')
    if not text_run:
        return ''
    return text_run.get('content')


def read_structural_elements(self, s_elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
        in nested elements.

        Args:
            elements: a list of Structural Elements.
    """
    text = ''
    for value in s_elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(self,p_element=elem)
        elif 'table' in value:
            # The text in table cells are in nested Structural Elements and tables may be nested.
            table = value.get('table')
            for row in table.get('tableRows'):
                cells = row.get('tableCells')
                for cell in cells:
                    text += read_structural_elements(self, s_elements=cell.get('content'))
        elif 'tableOfContents' in value:
            # The text in the TOC is also in a Structural Element.
            toc = value.get('tableOfContents')
            text += read_structural_elements(self, s_elements=toc.get('content'))
    return text
