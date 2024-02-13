class Solution:

    def gcd(a, b): # Recursive function to return gcd
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: # If No substring exists
            return ""
        l1, l2 = len(str1), len(str2)
        if str1 > str2:
            g = gcd(l1, l2)
            return str2[:g]
        else:
            g = gcd(l2, l1)
            return str1[:g]      
