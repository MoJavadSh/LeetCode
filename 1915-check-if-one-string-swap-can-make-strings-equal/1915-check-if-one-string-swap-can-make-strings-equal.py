class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2 :
            return True
        for i in range(0,len(s1)):
            for j in range(i+1,len(s1)): 
                tempS1 = list(s1)
                tempS2 = list(s2)
                tempS1[i], tempS1[j] = tempS1[j], tempS1[i]
                if tempS1 == tempS2 :
                    return True 
        return False

