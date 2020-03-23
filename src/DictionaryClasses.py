class DictEntry:
    def __init__(self,term,doc_freq,offset):
        self.term = term
        self.doc_freq = doc_freq
        self.offset = offset
    
    def __str__(self):
        return "Term: " + str(self.term) + " , Doc. Freq: " + str(self.doc_freq) + " , Offset: " + str(self.offset)