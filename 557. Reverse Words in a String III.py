class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        # print(type(s))
        for i in range(len(s)):
            s[i] = s[i][::-1]
        s = ' '.join(s)
        return s