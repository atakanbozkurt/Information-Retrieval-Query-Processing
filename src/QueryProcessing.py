from nltk.stem.porter import PorterStemmer
import os.path

'''
Auxiliary function to tokenize queries.
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

'''
Tokenize query and return list of tokens(query words).
'''
def TokenizeQuery(query):
    porter_stemmer = PorterStemmer()
    # 1)Input : "A new hi-gh for the sto-ck market?"
    # 2)Output : ["a","new","high","for","the","stock","market"]
    # remove all punctuation except "*"
    need_to_remove = r"""!"#$%&'()‘’+,-./:;<=>?@[\]^_`{|}~"""
    trantab = str.maketrans({key: None for key in need_to_remove})
    j = str.lower(query.translate(trantab))  # same as j = j.replace('single punctuation','') for many line & lower
    # print(line2)
    x = j.split()
    number_with_space = ""
    number_exist = False
    result = []
    # ADD ELEMENTS FOR EACH TITLE WITH LOGIC TO DISPOSE NUMBER WITH SPACE (EG. "607 123 4567")
    for i in x:
        if number_exist and not is_number(i):
            result.append(str(number_with_space))
            result.append(porter_stemmer.stem(i))
            number_with_space = ""
            number_exist = False
        elif not number_exist and not is_number(i):
            result.append(porter_stemmer.stem(i))
            number_exist = False
        elif is_number(i) and not number_exist:
            number_exist = True
            number_with_space = number_with_space + '' + str(i)
        elif is_number(i) and number_exist:
            number_with_space = number_with_space + '' + str(i)
    if number_exist:
        result.append(str(number_with_space))
        #     print(i)
    return result
