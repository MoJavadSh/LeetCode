class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while (i ** 2) <= x:
            i+=1
        return i-1
        
            