from DAATClasses import Result, QueryInfo
import math

<<<<<<< HEAD
def CosSim(terms_postings,tokens,normalized_docs,dictionary):
    '''
    #If you need to work with documents
    print("Largest doc Id in collection: " , normalized_docs[-1].docId)
    print("Available number of documents in the collection" , normalized_docs[-1].docId + 1)
    '''
    
    print("From dictionary find document frequency by using command below")
    term_entry = dictionary.get("ahead")
    print("ahead doc freq: ", term_entry.doc_freq)


    
=======
def CosSim(terms_postings,tokens):
>>>>>>> origin/master
    cos_sim = []
    doc_list = []
    tokens_info=[]
    N = len(terms_postings)
    tokens_set = set(tokens)

    for token in tokens_set:
        tftd = 0
        df = 0

        for t in tokens:
            if t == token:
                tftd = tftd + 1

        for t_p in terms_postings:
           if t_p.term == token:
               df +=1
        idfw = math.log10(N/int())
        info = QueryInfo(token, tftd, idfw)
        tokens_info.append(info)



    for i in terms_postings:
        if i.docid not in doc_list:
            doc_list.append(i.docid)
    doc_list.sort()

    #open one file each time
    for i in doc_list:
        qidi = 0
        n_sqr_di = 0
        di = 0  # the same ?
        for j in terms_postings:
            if j.docid == i:
                qi = searchqi(j.term, tokens_info)
                di = searchtfw(j.term, terms_postings) * 1 #how to get idfw
                qidi = qidi + qi*di # the sum of qi * di
                n_sqr_di = n_sqr_di + math.pow(n_sqr_di, 2) # the sum of di**2
        sim = qidi/math.sqrt(n_sqr_di)
        result = Result(i, sim)
        cos_sim.append(result)

    # need sort result by sim
    
    return cos_sim

def searchqi(term, tokens_info):
    for i in tokens_info:
        if term == i.token:
            return i.qi

def searchtfw(term, terms_postings):
    for i in terms_postings:
        if term == i.term:
            return i.tf_weight