class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        concat = ""
        idx = 0
        for i in range(len(word1)):
            if i < len(word2):
                concat += word1[i] + word2[i]
            else:
                concat += word1[i:]
                idx = i
                break
            idx = i

        if idx + 1 < len(word2):
            concat += word2[idx + 1:]

        return concat