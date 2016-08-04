#209. Minimum Size Subarray Sum
# -*- coding:utf-8 -*- 
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int  aco
        """
        size = len(nums)
        left, right = 0, size
        bestAns = 0
        while left <= right:
            mid = (left + right) / 2
            if self.solve(mid, s, nums):
                bestAns = mid
                right = mid - 1
            else:
                left = mid + 1
        return bestAns

    def solve(self, l, s, nums):
        sums = 0
        for x in range(len(nums)):
            sums += nums[x]
            if x >= l:
                sums -= nums[x - l]
            if sums >= s:
                return True
        return False
 

 #二分查找找到一个数，solve函数检测这个数是不是可以