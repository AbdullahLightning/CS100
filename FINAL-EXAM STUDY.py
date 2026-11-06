#34
def lengthStats(text):
    d={}
    newText = text.lower().split()
    for word in newText:
        length = len(word)
        if length is not in d:
            d[length] = [word]
        elif word not in d[length]:
            d[length].append(word)
    return d
someText = 'It is what it is'
print(lengthStats(someText))
#35
def longestWordInLine(name1, name2):
    inf = open(name1, 'r')
    outf = open(name2, 'w')
    for line in inf:
        words = line.split()
        for word in words:
            maxWord=''
            if len(word) >= len(maxWord):
                maxWord = line
        outf.write(maxWord +'\n')
         
    inf.close()
    outf.close()
#36
def wordDictFromFile(filename):
    inf = open(filename, 'r')
    d={}
    content = inf.read()
    pairList = content.split()
    for pair in pairList:
        tokens = pair.split(':')
        word=tokens[0]
        count=int(tokens[1])
        if word not in d:
            d[word] = count
        else:
            d[word]+= count
    inf.close()
    return d       
            
        
    
    
    
