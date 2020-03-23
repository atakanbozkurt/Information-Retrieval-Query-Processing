class Document:
    def __init__(self,term,docId,tf_weight):
        self.term = term
        self.docId = docId
        self.tf_weight = tf_weight

    
    def __str__(self):
        return "Term: " + str(self.term) + " , DocId: " + str(self.docId) + " , Tf Weight: " + str(self.tf_weight)