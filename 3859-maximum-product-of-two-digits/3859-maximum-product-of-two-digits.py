class Solution:
    def maxProduct(self, n: int) -> int:
        digits = list(map(int, str(n)))
        first = max(digits)
        digits.remove(first)
        second = max(digits)
        return first * second
        
        