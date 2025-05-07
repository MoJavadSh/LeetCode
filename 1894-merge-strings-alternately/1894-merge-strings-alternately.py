class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        mini = min(len(word1),len(word2))

        for i in range(0 , mini):
            merged += word1[i]
            merged += word2[i]
        
        if (len(word2) == mini):
            merged += (word1[mini : len(word1) + 1])
        else :
            merged += (word2[mini : len(word2) + 1])

        return merged