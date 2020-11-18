const deDupe = (wordList) => {
    const wordDict = {}
    wordList.forEach((word) => {
        wordDict[word] = 1
    })
    return Object.keys(wordDict)
}