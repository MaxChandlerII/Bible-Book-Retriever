#def hello_world():
    #return "Hello World!"
# import google
# import googlesearch
# Word Document Library
import docx
from sqlalchemy import false, true #I didn't add this. Python must've added for some reason.

#Word Doc Variables
doc = docx.Document("C:\Personal_Repos\Bible-Book-Retriever\Proverbs.docx")
proverbs_list = [ ] #A blank 2-D list. Zero index accesses a Chapter. 1st index accesses a Verse in the specified Chapter



'''
#Start of Google Search (make a F( ) )
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# to search
query = "BibleProject"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)

print("Finished search.")
#End of Google Search
'''

def get_number_verses(b_print):
    num_verses = doc.paragraphs
    num_verses = len(num_verses)
    if( true == b_print ):
        print("Number of verses = ", num_verses )
    return num_verses

def print_all_verses():
    #Print each verse in the Terminal
    for para in number_verses:
        print(number_verses.text)
        print("-------")

def get_all_verses():
    # reading each line    
    for line in doc:
        # reading each word        
        for word in line.split():
            # displaying the words           
            print(word) 

print("hello Max")
b_print = false
number_verses = 0
number_verses = get_number_verses( b_print )
print("# of Verses = ", number_verses)
get_all_verses()