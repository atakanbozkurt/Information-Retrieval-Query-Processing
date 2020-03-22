#Functions to calculate weight of a term used in a document
import os.path
from PostingsClasses import TermFrequencyWeight,DocumentLength


'''
Computes the logarithmic term frequency weight used in a document
'''
def GetTfWeights():
    tf_weights = []
    postings_path = os.path.abspath("../input_files/postings.txt")
    postings_file = open(postings_path,encoding='utf8')
    
    for line in postings_file:
        args = line.split()
        tf_weights.append(TermFrequencyWeight(args[0],args[1]))
    
    postings_file.close()

    return tf_weights


'''
For all documents, sums up term frequency weights used in that document and normalizes the length
'''
def NormalizeDocLength(tf_weights):
    normalized_docs = []
    #Do not mutate parameter
    tf_w = tf_weights[:]
    #Sort tf_w to iterate for every document
    tf_w.sort(key=lambda x:x.docId, reverse=False)
    doc_amount =  tf_w[len(tf_w)-1].docId

    #Check if it is sorted correctly
    for tf in tf_w:
        print(tf)
    print(len(tf_w),"\n++++++++++++++++++++++++++++++++++++++++++++\n")

    for i in range(len(tf_w)):
        docId = tf_w[i].docId
        tf_weight = tf_w[i].tf_weight


    return normalized_docs