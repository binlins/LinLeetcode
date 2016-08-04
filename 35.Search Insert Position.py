# -*- coding:utf-8 -*- 
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, hig = 0, len(nums)
        if nums[hig-1] < target:
            return hig
        while low <= hig:
            mid = (low + hig) / 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                hig = mid - 1
            elif nums[mid] == target:
                return mid
        return low
#基于二分查找   灵光乍现返回LOW,正好