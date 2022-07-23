#def hello_world():
    #return "Hello World!"
# import google
# import googlesearch
# Word Document Library
import docx
from sqlalchemy import false, true #I didn't add this. Python must've added for some reason.

#Word Doc Variables
doc = docx.Document("C:\Personal_Repos\Bible-Book-Retriever\Proverbs.docx")
pr10_list = [ ] #A blank 2-D list. Zero index accesses a Chapter. 1st index accesses a Verse in the specified Chapter
pr10_num_ver = 0 #will hold # verses found in Proverbs 10

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
    pr10_num_ver = doc.paragraphs
    pr10_num_ver = len(pr10_num_ver)
    if( true == b_print ):
        print("Number of verses = ", pr10_num_ver )
    return pr10_num_ver

def print_all_verses():
    #Print each verse in the Terminal
    pr10_num_ver = get_number_verses(false)
    for para in doc.paragraphs:
        print(doc.text)
        print("-------")

def get_all_verses():
    # reading each line    
    for line in doc:
        # reading each word        
        for word in line.split():
            # displaying the words           
            print(word) 

def getText( ):
#def getText(filename):
    #doc = docx.Document(filename)
    #fullText = []
    for para in doc.paragraphs:
        #fullText.append(para.text)
        pr10_list.append(para.text)
    #return '\n'.join(fullText)

'''
Intended Design
1) 2-D List, Zero index accesses a Chapter. 1st index accesses a Verse in the specified Chapter
2) Search for every strong's and remove from List
3) Find repeated words
    A) Start w/first English word and store in local var
    B) compare every word in that verse to it and every word in each subsequent verse and 
    C) Keep track # of times repeated
    D) remove the repeated word from the other verses? (to prevent redundant checking)
    E) Repeated Words
        - Keep a 2-D List w/repeated words, append words as detected. Store the word in index 0, store the verses in index 1.
        - Keep a 2-D List w/non-repeated words, append words as detected. Store the word in index 0, store the verses in index 1.
4) Print in terminal the repeated words and non-repeated words
5) Store in word doc the repeated words
6) Highlight repeated words. If "wisdom" is repeated 10 times in the chapter, highlight all occurances same color. Each word and all of its occurances get a unique color
'''

# Defining main function
def main():
    print("hello Max")
    '''b_print = true
    get_number_verses( b_print )
    print_all_verses()'''
    getText()
    i = 0
    for i in range(31):
        '''proverbs_list[i] = doc.paragraphs[i]
        print("proverbs_list[",i,"] = ",pr10_list[i] )'''
        print("proverbs_list[",i,"] = ",pr10_list[i] )
        #if( ) #pull the verse # out of proverbs list, then store the verse words in other column
        #don't think i need a F( ) to traverse to get the length of pr10, i think there's a var in the doc or para var for len already

  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()