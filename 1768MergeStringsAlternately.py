class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0 # Pointer variables to iterate over both strings
        ans = "" # empty string to store final answers
        l1, l2 = len(word1), len(word2) # variables to store lengths of strings which we gonna use twice

        while i < l1 and j < l2: # looping until end of 1 string is reached
            ans += word1[i] + word2[j]
            i += 1
            j += 1

        if i < l1: # If any elements of string1 are not reached they will be concatinated here
            ans += word1[i:] 

        if j < l2: # If any elements of string2 are not reached they will be concatinated here
            ans += word2[j:]

        return ans
        
