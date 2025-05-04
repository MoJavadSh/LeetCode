class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_result = ""
        for i in range(len(number)):
            if number[i] == digit:
                new_number = number[:i] + number[i+1:]  # Remove the digit at index i
                if new_number > max_result:  # Lexicographical comparison works for numbers as strings
                    max_result = new_number
        return max_result