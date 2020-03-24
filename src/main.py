import os.path
import sys
from WeightFunctions import GetTfWeights, NormalizeDocLength
from DictionaryFunctions import BuildDictionary
from QueryProcessing import TokenizeQuery
from PostingsFunctions import GetAllPostings
from DAATFunctions import CosSim


def main():
    
    if len(sys.argv) < 2:
        print("Command line usage: python main.py 'query terms' ")
        sys.exit()
    else:
        query = ""
        queries = sys.argv
        queries.pop(0)
        for q in queries:
            query += q + " "   
        #print(query)
    
    
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
    #6)Implement the Document-At-A-Time algorithm for processing vector space queries based on the Cosine similarity function.
    cos_sim = CosSim(terms_postings,tokens,normalized_docs,dictionary)
    #7) Write similarities to result
    WriteResult(cos_sim,query)


    #For submission: Write dictionary, tf_weights and normalized_docs into file
    WriteDictionary(dictionary)
    WriteTfWeight(tf_weights)
    WriteNormalizedDocs(normalized_docs)


    #Comment out if you want to see results on terminal
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
    
    print("-------------   Tokenization   --------------------")
    print("Query: ", query , "\nTokens: " , tokens)
    
    print("-------------   Term - Postings List    --------------------")
    for postings in terms_postings :
        for documents in postings:
            print(documents)
    '''
    print("-------------   CosSim    --------------------")
    print("Query: ",query)
    topK = 0
    for doc in cos_sim:
        if topK == 10:
            break
        print(doc)
        topK += 1


    return


'''
Write TOP 10 similarities results into file
'''
def WriteResult(cos_sim,query):
    file = os.path.abspath("../output_files/query_result.txt")
    f = open(file,"w")
    q = "Query: " + query + "\n"
    f.write(q)
    counter = 0
    for doc in cos_sim:
        if counter == 10:
            break
        line = "DocId: " + str(doc.docId) + "  Cos_Similarity: " + str(doc.cos_sim) + "\n"
        counter += 1
        f.write(line)
    f.close()
    return

def WriteDictionary(dictionary):
    file = os.path.abspath("../output_files/dictionary.txt")
    f = open(file,"w")
    header = "Dictionary: \n"
    f.write(header)

    for entry in dictionary:
        e = dictionary.get(entry)
        line = str(e) + "\n" 
        f.write(line)
    f.close()
    return

def WriteTfWeight(tf_weights):
    file = os.path.abspath("../output_files/tf_weights.txt")
    f = open(file,"w")
    header = "Term frequency weights:\n"
    f.write(header)

    for t in tf_weights:
        line = "Doc Id: " + str(t.docId) + "  Frequency: " + str(t.frequency) + " Weight: " + str(t.tf_weight) + " \n"
        f.write(line)
    f.close()
    return
    
def WriteNormalizedDocs(normalized_docs):
    file = os.path.abspath("../output_files/normalized_docs.txt")
    f = open(file,"w")
    header = "Document Normalization: \n"
    f.write(header)
    for doc in normalized_docs:
        line = str(doc) + "\n"
        f.write(line)
    f.close()
    return


if __name__ == "__main__":
    main()