from DAATClasses import Result, QueryInfo
import math

def CosSim(terms_postings,tokens,normalized_docs,dictionary):
    '''
    #If you need to work with documents
    print("Largest doc Id in collection: " , normalized_docs[-1].docId)
    print("Available number of documents in the collection" , normalized_docs[-1].docId + 1)
    
    print("From dictionary find document frequency by using command below")
    term_entry = dictionary.get("ahead")
    print("ahead doc freq: ", term_entry.doc_freq)
    '''

    cos_sim = []
    doc_list = []
    tokens_info=[]
    N_Q = 0
    for docments in terms_postings:
        N_Q = N_Q + len(docments)
    # print(N_Q)
    N_D = len(normalized_docs)
    tokens_set = set(tokens)

    for token in tokens_set:
        tftd = 0
        df = 0

        for t in tokens:
            if t == token:
                tftd = tftd + 1

        for t_p in terms_postings:
            for documents in t_p:
                # print(documents.term+" token:"+token)
                if documents.term == token:
                    df +=1
                    # print("df="+str(df))
        if df == 0:
            idfw = 0
        else: idfw = math.log10(N_Q/int(df))
        # print(N_Q/int(df))
        info = QueryInfo(token, tftd, idfw)
        tokens_info.append(info)
    # for i in tokens_info:
    #     print(i)



    for i in terms_postings:
        for documents in i:
            if documents.docId not in doc_list:
                doc_list.append(documents.docId)
    doc_list.sort()

    #open one file each time
    for i in doc_list:
        qidi = 0
        n_sqr_di = 0
        for j in terms_postings:
            for documents in j:
                if documents.docId == i:
                    qi = searchqi(documents.term, tokens_info)
                    # print("qi:" + str(qi))
                    di = float(searchtfw(documents.term, terms_postings)) * math.log10(N_D/int(dictionary.get(documents.term).doc_freq))
                    # print(math.log10(N_D/int(dictionary.get(documents.term).doc_freq)))
                    qidi = qidi + qi*di # the sum of qi * di
                    n_sqr_di = n_sqr_di + math.pow(di, 2) # the sum of di**2
        # if qidi != 0:
        # print(str(qidi) + " " + str(n_sqr_di))
        sim = qidi/math.sqrt(n_sqr_di)
        result = Result(i, sim)
        cos_sim.append(result)

    # need sort result by sim
    cos_sim.sort(reverse=True)
    
    return cos_sim

def searchqi(term, tokens_info):
    for i in tokens_info:
        if term == i.token:
            return i.qi

def searchtfw(term, terms_postings):
    for i in terms_postings:
        for docments in i:
            if term == docments.term:
                return docments.tf_weight