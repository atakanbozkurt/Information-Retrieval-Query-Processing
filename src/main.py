import os.path
from WeightFunctions import GetTfWeights, NormalizeDocLength
from DictionaryFunctions import BuildDictionary
from QueryProcessing import TokenizeQuery
from PostingsFunctions import GetAllPostings
from DAATFunctions import CosSim


def main():
    query = "10year 2008style asia"

    #1)Read dictionary.txt and use hash table to implement a dictionary
    dictionary = BuildDictionary()
    #2) Read postings.txt" to compute term frequency weight
    tf_weights = GetTfWeights()
    #3) Sum term weights used in a document and normalize the length
    normalized_docs = NormalizeDocLength(tf_weights)
    #4) Parse input queries
    tokens = TokenizeQuery(query)
    #5) Find the correct postings list for any query term
    terms_postings = GetAllPostings(dictionary,tokens,tf_weights)


    
    print("-------------   Dictionary    --------------------")
    for e in dictionary:
        print(e,"--> ", dictionary[e])
    

    print("\n\n-------------   Tf_Weights    --------------------")
    for e in tf_weights:
        print(e)
    
    print("\n\n-------------   Normalized doc length   --------------------")
    for n in normalized_docs:
        print(n)


    print("-------------   Tokenization   --------------------")
    print("Query: ", query , "\nTokens: " , tokens)
    
    print("-------------   Term - Postings List    --------------------")
    for postings in terms_postings :
        for documents in postings:
            print(documents)

    #6)Implement the Document-At-A-Time algorithm for processing vector space queries based on the Cosine similarity function.
    print("-------------   CosSim    --------------------")
<<<<<<< HEAD
    cos_sim = CosSim(terms_postings,tokens,normalized_docs,dictionary)
    #for doc in cos_sim:
    #    print(doc)

=======
    # cos_sim = CosSim(terms_postings,tokens)
    # for doc in cos_sim:
    #     print(doc)
>>>>>>> origin/master

    return

if __name__ == "__main__":
    main()