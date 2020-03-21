import math


class TermFrequencyWeight:

    def __init__(self, docId, frequency):
        self.docId = docId
        self.frequency = frequency
        self.tf_weight = 1 + math.log10(int(frequency))

    def __str__(self):
        return "DocId: " + str(self.docId) + " ,  Frequency: " + str(self.frequency) + " ,  Tf Weight: " + str(
            self.tf_weight)