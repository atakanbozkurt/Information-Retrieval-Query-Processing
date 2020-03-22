import os.path
from WeightFunctions import GetTfWeights, NormalizeDocLength
from DictionaryFunctions import BuildDictionary
from QueryProcessing import TokenizeQuery


def main():
    query = "TI shares decline in late trading; H-P rises 914 479 73 60"

    #1)Read dictionary.txt and use hash table to implement a dictionary
    dictionary = BuildDictionary()
    #2) Read postings.txt" to compute term frequency weight
    tf_weights = GetTfWeights()
    #3) Sum term weights used in a document and normalize the length
    normalized_docs = NormalizeDocLength(tf_weights)
    #4) Parse input queries
    tokens = TokenizeQuery(query)
    #5) Find the correct postings list for any query term
    #~~~~

    ''' 
    print("-------------   Dictionary    --------------------")
    for e in dictionary:
        print(e,"--> ", dictionary[e])

    print("\n\n-------------   Tf_Weights    --------------------")
    for e in tf_weights:
        print(e)
    
    print("\n\n-------------   Normalized doc length   --------------------")
    for n in normalized_docs:
        print(n)
    '''
    print("-------------   Tokenization   --------------------")
    print("Query: ", query , "\nTokens: " , tokens)



    return

if __name__ == "__main__":
    main()