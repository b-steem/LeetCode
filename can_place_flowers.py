class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i - 1 >= 0 and flowerbed[i - 1] == 0) or i - 1 < 0:
                    if (i + 1 < length and flowerbed[i + 1] == 0) or i + 1 >= length:
                        flowerbed[i] = 1
                        count += 1
        
        return count >= n