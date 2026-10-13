class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}
        for ch in s:
            if ch in hashmaps:
                hashmaps[ch] +=1
            else:
                hashmaps[ch] = 1
        for ch in t:
            if ch in hashmapt:
                hashmapt[ch] +=1
            else:
                hashmapt[ch] = 1
        if hashmaps == hashmapt:
            return True
        else:
            return False            
                            