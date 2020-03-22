import os.path
from ComputeWeights import GetTfWeights, NormalizeDocLength
from DictionaryFunctions import BuildDictionary

def main():

    #1)Read dictionary.txt and use hash table to implement a dictionary
    dictionary = BuildDictionary()

    for e in dictionary:
        print(e,"--> ", dictionary[e])
    print("\n-----------------------------------\n")

    #2) Read postings.txt" to compute term frequency weight
    tf_weights = GetTfWeights()

    for e in tf_weights:
        print(e)

    
    #3) Sum term weights used in a document and normalize the length
    #normalized_docs = NormalizeDocLength(tf_weights)

    #for n in normalized_docs:
    #    print(n)


    return

if __name__ == "__main__":
    main()