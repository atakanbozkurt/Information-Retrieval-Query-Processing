import os.path
from DictionaryClasses import DictEntry


'''
Build dictionary using hash table. Key is term. Value is object of term,docId,offset(pointer) to postings
'''
def BuildDictionary():
    dictionary_path = os.path.abspath("../input_files/dictionary.txt")
    dictionary_file = open(dictionary_path,encoding='utf8')
    dictionary = {}
    for line in dictionary_file:
        args = line.split()
        term = args[0]
        doc_freq = args[1]
        offset = args[2]
        dictionary[term] = DictEntry(term,doc_freq,offset)
   
    dictionary_file.close()

    return dictionary