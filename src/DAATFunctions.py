from DAATClasses import Result
import math

def CosSim(terms_postings, tokens):
    cos_sim = []
    doc_list = []
    for i in terms_postings:
        if i.docid not in doc_list:
            doc_list.append(i.docid)
    for i in doc_list:
        qidi = 0
        l_sqr_di = 0
        for j in tokens:
        # if token j in doc i, calc sim
        sim = qidi/math.sqrt(math.pow(l_sqr_di, 2))
        result = Result(i, sim)
        cos_sim.append(result)
        # need sort result by sim
    return cos_sim
