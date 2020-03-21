#Functions to calculate weight of a term used in a document
import os.path


#Computes the term frequency weight used in a document
def TermFrequencyWeight():
    postings_path = os.path.abspath("../input_files/postings.txt")
    postings_file = open(postings_path,encoding='utf8')
    
    for line in postings_file:
        print(line)
    
    return
