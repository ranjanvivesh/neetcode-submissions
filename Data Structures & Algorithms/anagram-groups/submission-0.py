class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        imap = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in imap:
                imap[key] = []

            imap[key].append(word)

        result = []

        for value in imap.values():
            result.append(value)
        return result                