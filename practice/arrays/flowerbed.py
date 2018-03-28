class Solution:
    def is_available(self, flowerbed, n):
        i, count = 0, 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                i += 1
                count += 1
            if count >= n:
                return True
            i += 1
        return False


s = Solution()
print(s.is_available([1,0,0,0,0,1], 2))