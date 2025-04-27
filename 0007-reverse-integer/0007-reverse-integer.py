class Solution:
    def reverse(self, x: int) -> int:
        num = x
        neg = False
        if num < 0 :
            num = abs(num)
            neg = True
        rev_num = 0
        while num != 0 :
            digit = num % 10
            rev_num = rev_num * 10 + digit
            num //= 10
        if rev_num < (-2**31) or rev_num > (2**31 - 1):
            return 0
        else : 
            if neg : return (rev_num * -1)
            else : return (rev_num)
        