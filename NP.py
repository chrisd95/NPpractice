sentence = "A lion attacked Jane in the zoo"

dictionnary = {
"lion" : "N",
"knife": "N",
"zoo": "N",
"attacked": "V",
"Jane":"PN",
"the":"DET",
"A":"DET",
"with":"PREP",
"in":"PREP"
};

def sentenceLister(sentence):
    sentenceList = []
    block = []
    for i in range(len(sentence)):
        if sentence[i] != " ":
            block.append(i)
        else:
            block.append(i)
            sentenceList.append(sentence[block[0]:block[-1]])
            block = []
        if i == len(sentence)-1:
            block.append(i+1)
            sentenceList.append(sentence[block[0]:block[-1]])
            block = []
    return sentenceList

sentenceList = sentenceLister(sentence)

print(sentenceList)

def parser(sentenceList):
    parsedSentence = []
    for i in range(len(sentenceList)):
        lookUp = dictionnary[sentenceList[i]]
        parsedSentence.append(lookUp)
    return parsedSentence
parsedSentence = parser(sentenceList)

print(parsedSentence)
