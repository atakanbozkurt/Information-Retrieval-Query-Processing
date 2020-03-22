import math


class TermFrequencyWeight:
    def __init__(self,docId,frequency):
        self.docId = int(docId)
        self.frequency = int(frequency)
        self.tf_weight = 1 + math.log10(int(frequency))
    
    def __str__(self):
        return "DocId: " + str(self.docId) + " ,  Frequency: " + str(self.frequency) + " ,  Tf Weight: " + str(self.tf_weight)


class DocumentLength:
    def __init__(self,docId,tf_weight):
        self.docId = docId
        self.length = 1/(math.sqrt(tf_weight))
        self.tf_sum = (tf_weight)*(tf_weight)

    def __str__(self):
        return "DocId: " + str(self.docId) + " , Length: " + str(self.length)
    
    def UpdateLength(self,tf_weight):
        self.tf_sum += (tf_weight)*(tf_weight)
        self.length = 1/(math.sqrt(tf_sum))
