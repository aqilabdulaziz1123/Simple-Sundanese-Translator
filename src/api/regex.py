import re

def translateregex(sentence,ldict):
    for word in ldict:
        sentence = re.sub(word,ldict[word],sentence)
    return sentence