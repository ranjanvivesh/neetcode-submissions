class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}
        for i in range(len(s)):
            if s[i] in freqS:
                freqS[s[i]] += 1
            else:
                freqS[s[i]] = 1

        for j in range(len(t)):
            if t[j] in freqT:
                freqT[t[j]] += 1
            else:
                freqT[t[j]] = 1
        
        return freqS == freqT          


        