# Functions to calculate weight of a term used in a document
import os.path
from Classes import TermFrequencyWeight

'''
Computes the logarithmic term frequency weight used in a document
'''


def GetTfWeights():
    tf_weights = []
    postings_path = os.path.abspath("../input_files/postings.txt")
    postings_file = open(postings_path, encoding='utf8')

    for line in postings_file:
        args = line.split()
        tf_weights.append(TermFrequencyWeight(args[0], args[1]))

    postings_file.close()

    return tf_weights


'''
For all documents, sum up term frequency weights and normalizes the length
'''


def NormalizeDocLength(tf_weights):
    # Find the the number of documents by finding the max docId
    # Do not mutate parameter
    tf_w = tf_weights[:]
    tf_w.sort(key=lambda x: x.docId)

    # Check if it is sorted correctly
    for tf in tf_w:
        print(tf)
    print(len(tf_w))

    normalized_docs = []

    return normalized_docs