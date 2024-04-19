class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) < 2:
            return s
        newList = []
        for x in s:
            if x == '*':
                newList.pop()
            else:
                newList.append(x)
        
        return "".join(newList)
