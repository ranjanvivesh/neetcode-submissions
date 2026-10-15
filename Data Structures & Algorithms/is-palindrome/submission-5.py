class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if ch.isalnum():
                result += ch.lower()
        l = 0
        r = len(result)-1
        while l < r:
            if result[l] != result[r]:
                return False
            l += 1
            r -= 1
        return True        