class Solution:
    def isPalindrome(self, x: int) -> bool:
        xr = str(x)
        rev = xr[::-1]
        print(rev)
        if xr == rev :
            return True
        else : return False