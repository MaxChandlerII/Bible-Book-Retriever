from posixpath import split
import os, re, csv

class Text_Wrangling:
    def __init__(self) -> None:
        pass

    def rep_words_occurance(local_doc):
        ldoc_list = [] #Create a list for the Local Doc's content

        if os.path.isfile(local_doc):
            '''
            file    =   _io.TextIOWrapper
            line    =   str
            word    =   tuple
            ldoc_list[]  =   list
            ldoc_list[i] =   tuple (I don't think this is true anymore now that I separate the # from the Text and only store the Text in ldoc_list[] )
            '''
            with open(local_doc,'r') as file: 
                for line in file:
                    for word in enumerate(line.split()):
                        temp_num, temp_text = word #word is a Tuple. Separate the # from the Text.
                        ldoc_list.append( temp_text ) #Store the Text in list. 
                        #Perhaps there's something useful with the # (number)

                print('length of ldoc_list[] = %s' %str(len(ldoc_list)) ) #Print length of ldoc_list string

                '''
                (1) Loop through ldoc_list list
                (2) Find number of times each word appears in this Text (print this)
                (3) Open a .csv and record each word and the number of times it occurs
                '''
                for index in range( len(ldoc_list) ):
                    num_occurances = ldoc_list.count( ldoc_list[index] )
                    # print( "word = '%s' appears %s in ldoc_list[]" %( ldoc_list[index], num_occurances) )
                    print("word = '{cword}' appears {times} in ldoc_list[]".format(cword=ldoc_list[index], times=str(num_occurances) ) )
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
                        tempList.insert(0,ldoc_list[index])
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