def lps(pat):
    ar = [0 for i in pat]
    for i in range(len(ar)):
        stop = False
        for j in range(i+1,len(ar)):
            if pat[i] == pat[j] and ar[j-1] == i:
                stop = True
                ar[j] = 1 + ar[j-1]
                # print(i,j)
        if not stop:
                break
    return ar

def kmp(st,pat):
    lp = lps(pat)
    i = 0
    j = 0
    pos = []
    while ( i < len(st)):
        if st[i] == pat[j]:
            i += 1
            j += 1
        elif st[i] != pat[j]:
            if j == 0:
                i+=1
            else:
                j = lp[j-1]
            
        if j == len(pat):
            # print(i-len(pat))
            pos.append(i-len(pat))
            break
            # count += 1
            j = 0
    return pos

def translate(sentence,ldict):
    # print(sentence)
    for word in ldict.keys():
        # if word=="adik" :print("hai")
        x = kmp(sentence,word)
        if x:
            for place in x:
                sentence = translateword(sentence,place,ldict) 
    return sentence


def translateword(sentence,i,dict):
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
    return sentence.replace(kata,dict[kata])