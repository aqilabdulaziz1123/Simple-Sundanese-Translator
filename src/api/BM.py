def badH(pattern):
    dic = {}
    for i in range(len(pattern)):
        dic[pattern[i]] = i
    return dic


def badHS(txt,pat):
    # print(txt)
    m = len(pat) 
    n = len(txt)
    badChar = badH(pat)
    s = 0
    while(s <= n-m): 
        j = m-1
        while j>=0 and pat[j] == txt[s+j]: 
            j -= 1
        if j >= 0:
            if (txt[s+j] in badChar.keys()):
                s += max(1,j - badChar[txt[s+j]])
            else:
                s += 1
        else:
            return s

    return None

def getword(sentence,i,dict):
    j = i
    awal = j
    while sentence[j] != ' ':
        j -= -1
        if j == len(sentence):
            break
    akhir = j
    kata = ""
    for i in range(awal,akhir):
        kata += sentence[i]
    return kata

def translateBM(sentence,ldict):
    kata = []
    for word in ldict:
        x = badHS(sentence,word)
        if x != None and sentence[x] != " ":
            print(word)
            # print(word)
            kata.append(getword(sentence,x,ldict))
            print(kata)
            # sentence = translateword(sentence,x,ldict)
    for katakata in kata:
        sentence = sentence.replace(katakata,ldict[katakata])
    return sentence