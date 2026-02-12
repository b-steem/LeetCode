class Solution:
    def reverseVowels(self, s: str) -> str:
        idx = []
        for i in range(len(s)):
            if s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                idx.append(i)
        
        s = list(s)
        i = 0
        length = (len(idx) + 1) // 2
        while i < length:
            low = idx[i]
            high = idx[len(idx) - i - 1]
            temp = s[low]
            s[low] = s[high]
            s[high] = temp

            i += 1

        new_str = ""
        for i in range(len(s)):
            new_str += s[i]
        return new_str