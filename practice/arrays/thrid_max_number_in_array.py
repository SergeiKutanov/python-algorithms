class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = None
        max2 = None
        max3 = None
        for n in nums:
            if n == max1 or n == max2 or n == max3:
                continue
            if max1 is None or n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif max2 is None or n > max2:
                max3 = max2
                max2 = n
            elif max3 is None or n > max3:
                max3 = n
        if max3 is not None:
            return max3
        return max1

s = Solution()
print(s.thirdMax([3,3,4,3,4,3,0,3,3]))