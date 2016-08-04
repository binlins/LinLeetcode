#162. Find Peak Element
#-*- coding:utf-8 -*-
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tmpI = 0
        # for i in xrange(len(nums)):
        #     if nums[i] > nums[tmpI]:
        #         tmpI = i
        # return tmpI        
    #two
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right)/2
        #     if (mid == 0 or nums[mid] >= nums[mid - 1]) and (mid == len(nums) -1 or nums[mid] >= nums[mid + 1]):
        #         return mid
        #     elif mid > 0 and nums[mid-1] > nums[mid]:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return 0
    #three
        low, hig = 0, len(nums) - 1
        while low < hig:
            mid = low + (hig-low)/2;
            if nums[mid] > nums[mid+1]:
                hig = mid
            else:
                low = mid + 1
        
        return low
        #三种方法，二分确实没怎么想到
    #four
        return self.Helper(nums, 0, len(nums)-1)
    
    def Helper(self, nums, low,  high):
        if low == high:
            return low
        mid = low + (high-low)/2
        if nums[mid] > nums[mid+1]:
            return self.Helper(nums, low, mid)
        else:
            return self.Helper(nums, mid+1, high)
    
    