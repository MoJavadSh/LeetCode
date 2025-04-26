# Last updated: 4/26/2025, 4:52:20 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        list = []
        for i in s:
            if i.isalnum():
                list.append(i)
        if list == list[::-1]:
            return True
        else:
            return False
