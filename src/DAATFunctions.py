from DAATClasses import Result
import math

def CosSim(terms_postings):
    cos_sim = []
    doc_list = []

    for i in terms_postings:
        if i.docid not in doc_list:
            doc_list.append(i.docid)
    doc_list.sort()

    #open one file each time
    for i in doc_list:
        qidi = 0
        n_sqr_di = 0
        for j in terms_postings:
            if j.docid == i:
                qi = 0 # tf*idf ?
                di = 0 # the same ?
                qidi = qidi + qi*di # the sum of qi * di
                n_sqr_di = n_sqr_di + math.pow(n_sqr_di, 2) # the sum of di**2
        sim = qidi/math.sqrt(n_sqr_di)
        result = Result(i, sim)
        cos_sim.append(result)

    # need sort result by sim

    return cos_sim
