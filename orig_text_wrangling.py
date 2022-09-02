

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