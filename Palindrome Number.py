class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_str = str(x)[::-1]
        if x < 0:
            return False
        
        reversed_str = str(x)[::-1]
        return str(x) == reversed_str