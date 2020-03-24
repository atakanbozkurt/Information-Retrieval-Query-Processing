from DAATClasses import Result, QueryInfo
import math

def CosSim(terms_postings,tokens):
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
        qi = 0  # tf*idf ?
        di = 0  # the same ?
        for j in terms_postings:
            if j.docid == i:
                qidi = qidi + qi*di # the sum of qi * di
                n_sqr_di = n_sqr_di + math.pow(n_sqr_di, 2) # the sum of di**2
        sim = qidi/math.sqrt(n_sqr_di)
        result = Result(i, sim)
        cos_sim.append(result)

    # need sort result by sim

    return cos_sim
