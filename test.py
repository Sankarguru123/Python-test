def get_words(input_file):
    """Function to get the words from input file"""
    try:
        output_list = []
        with open(input_file, "r") as file:
            #read content of file to string
            data = file.read().strip().lower()
            #Monitor Punctuations
            punctuation = """!"#$%&'()*+,./:;<=>?@[\]^_`{|}~"""
            data = data.translate(str.maketrans('', '', punctuation))
            words = data.split()
            # Get the unique words
            unique_words = set(words)
            output_list.append("The total wordcount :"+str(len(words))+"\n")
            output_list.append("Total of unique words :"+str(len(unique_words))+"\n")
            word_dict=dict()
            # get number of occurrences of the substring in the string
            for word in unique_words:
                occurrences = data.count(word)
                word_dict[word] = str(occurrences)
            # Make output as decending
            final_dict = dict(sorted(word_dict.items(), key=lambda item: item[1],reverse=True))
            output_list.append("------------Top 10 Words------------\n")
            # Check if output length not exceeded 10
            count = 0
            for final in final_dict:
                count+=1
                if count<=10:
                    output_list.append(str(final)+' : '+str(final_dict[final])+'\n')
        # Open the output file for write
        output = open("wc_report.txt", "w")
        output.writelines(output_list)
    except Exception as error:
        raise error

words = get_words(input_file="alice.txt")






















