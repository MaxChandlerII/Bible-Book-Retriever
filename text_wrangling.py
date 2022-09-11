import os, re, csv

class Text_Wrangling:
    def __init__(self) -> None:
        pass

    def rep_words_occurance(self, local_doc ):
        ldoc_list = [] #Create a list for the Local Doc's content

        if os.path.isfile( local_doc ):
            '''
            file    =   _io.TextIOWrapper
            line    =   str
            word    =   tuple
            ldoc_list[]  =   list
            ldoc_list[i] =   tuple (I don't think this is true anymore now that I separate the # from the Text and only store the Text in ldoc_list[] )
            '''
            word_idx = 0 #Location of the word will be 0 index. 
            re_idx = 1 #Location of Commas/Periods/Colons/Brackets/etc. that are parsed in re.split()
            spec_words = {'A': ["Apple", "apple"],'L': ["LORD","Lord"]}
            

            with open(local_doc,'r') as file: 
                for line in file:
                    for word in re.split(r"[\s,;.\[\]]+", line):
                        regex_word = str( word )
                        if(not (regex_word and not regex_word.isspace()) ):
                            break
                        first_char = regex_word[:1] #take the first character of the word index to use as Dictionary Key

                        if len(ldoc_list) == 0:
                            ldoc_list.append( regex_word )
                        else:
                            '''
                            Using first_char, 
                            look in the Dictonary using spec_words.get
                            not sure if you'll get a list or a single string, so may have to type check the return to know if we'll be iterating or single comparing
                            half focused implemented the d_list check from 68-71 but haven't tested, may've messed something up.
                            '''
                            idx = 0
                            for x in range( len(ldoc_list) ):
                                idx += 1
                                # if( ldoc_list[x].lower() == regex_word.lower() ):
                                #     break
                                # else:
                                #     idx += 1 #Increment counter, if it reaches value of len(list) then no match was found, so we'll append the word with confidence of no duplicate
                            if len(ldoc_list) == idx:
                                ldoc_list.append( regex_word ) #Store the Text in list.
                        # print('temp_reExp_rtrn = %s' %temp_reExp_rtrn)
                        #TODO: Perhaps there's something useful with the # (number)

                # print('length of ldoc_list[] = %s' %str(len(ldoc_list)) ) #Print length of ldoc_list string

            '''
            (1) Loop through ldoc_list list
            (2) Find number of times each word appears in this Text (print this)
            (3) Open a .csv and record each word and the number of times it occurs
            '''
            for index in range( len(ldoc_list) ):
                num_occurances = ldoc_list.count( ldoc_list[index] )
                # print( "word = '%s' appears %s in ldoc_list[]" %( ldoc_list[index], num_occurances) )
                # print("word = '{cword}' appears {times} in ldoc_list[]".format(cword=ldoc_list[index], times=str(num_occurances) ) )
                with open('word_occurance_count.csv', 'a', newline='', encoding='utf-8') as f:
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
                    TODO:
                    (1) Put all Text Wrangling into separate F( ), maybe even a Text Wrangling Class
                    (4) If you already wrote a word in the .csv, then don't write it again, since it'll be duplicate data.

                    '''
        else:
            print('Local File does NOT exist.')