import os.path
from WeightFunctions import GetTfWeights, NormalizeDocLength
from DictionaryFunctions import BuildDictionary

def main():

    #1)Read dictionary.txt and use hash table to implement a dictionary
    dictionary = BuildDictionary()

    print("-------------   Dictionary    --------------------")
    for e in dictionary:
        print(e,"--> ", dictionary[e])
    

    #2) Read postings.txt" to compute term frequency weight
    tf_weights = GetTfWeights()

    print("\n\n-------------   Tf_Weights    --------------------")
    for e in tf_weights:
        print(e)
    
    
    #3) Sum term weights used in a document and normalize the length
    normalized_docs = NormalizeDocLength(tf_weights)
    
    print("\n\n-------------   Normalized doc length   --------------------")
    for n in normalized_docs:
        print(n)

    return

if __name__ == "__main__":
    main()