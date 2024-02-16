class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        newF = [0] + flowerbed + [0]

        for i in range(1, len(newF)-1):
            if newF[i-1] == 0 and newF[i] == 0 and newF[i+1] == 0:
                newF[i] = 1
                n -= 1
    
        return n <= 0
