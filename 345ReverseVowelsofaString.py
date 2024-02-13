class Solution:
    def reverseVowels(self, s: str) -> str:
        start, end = 0, len(s)-1
        s = list(s)
        
        while(start < end):
            if s[start] in "aAeEiIoOuU" and s[end] in "aAeEiIoOuU":
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif s[start] in "aAeEiIoOuU":
                end -= 1
            elif s[end] in "aAeEiIoOuU":
                start += 1
            else:
                start += 1
                end -= 1
        return ''.join(s)
            
        
