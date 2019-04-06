sentence = "A lion attacked Jane in the zoo"

print("Raw Data: " + sentence)

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

grammar = {
"NPVP": "S",
"V": "VP",
"VNP":"VP",
"VPPP":"VP",
"DETN":"NP",
"PN":"NP",
"NPPP":"NP",
"PREPNP":"PP"
}

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

print("Listify: " + str(sentenceList))

def parser(sentenceList):
    parsedSentence = []
    for i in range(len(sentenceList)):
        lookUp = dictionnary[sentenceList[i]]
        parsedSentence.append(lookUp)
    return parsedSentence
parsedSentence = parser(sentenceList)

print("Parsed: " + str(parsedSentence))

def parseTrees(parsedSentence):
    matchedparsedSentence = []
    matchedparsedSentence2 = []
    for i in range(len(parsedSentence)):
        if i%2==0 and i < len(parsedSentence)-1:
            match = parsedSentence[i] + parsedSentence[i+1]
            matchedparsedSentence.append(match)
    if len(parsedSentence)%2 == 1:
        matchedparsedSentence.append(parsedSentence[-1])

    if len(parsedSentence)%2 == 1:
        matchedparsedSentence2.append(parsedSentence[0])
    for i in range(len(parsedSentence)):
        if i%2==1 and i < len(parsedSentence)-1:
            match = parsedSentence[i] + parsedSentence[i+1]
            matchedparsedSentence2.append(match)
    if len(parsedSentence)%2 == 1:
        matchedparsedSentence2.append(parsedSentence[-1])

    print("Bottom-up 1: " + str(matchedparsedSentence))

    print("Bottom-up 2: " + str(matchedparsedSentence2))

    for i in range(len(matchedparsedSentence)):
        if matchedparsedSentence[i] in grammar:
            lookUp = grammar[matchedparsedSentence[i]]
            matchedparsedSentence[i] = lookUp

    print(matchedparsedSentence)



parseTrees(parsedSentence)
