class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        strList = sentence.split()
        for i in range(len(strList)):
            if strList[i].startswith(searchWord):
                return i+1
        return -1