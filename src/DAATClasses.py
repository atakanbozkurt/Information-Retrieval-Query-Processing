import math
class Result:
    def __init__(self, docId, cos_sim):
        self.docId  = docId
        self.cos_sim= cos_sim

    def __str__(self):
        return "DocId: " + str(self.docId) + " , cos_sim: " + str(self.tf_weight)

class QueryInfo:
    def __init__(self, token, tf, idfw):
        self.token  = token
        self.tfw    = 1 + math.log10(int(tf))
        self.idfw   = idfw