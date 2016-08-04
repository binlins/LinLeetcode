#4. Median of Two Sorted Arrays
# -*- coding:utf-8 -*-
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.findKth(nums1, nums2, (len(nums1) + len(nums2)) / 2 + 1)
        else:
            return (self.findKth(nums1, nums2, (len(nums1) + len(nums2)) / 2) + \
                self.findKth(nums1, nums2, (len(nums1) + len(nums2)) / 2 + 1)) * 0.5
    def findKth(self, A, B, k):
        if len(A) < len(B):
            A, B = B, A
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
            
        pb = min(k/2, len(B))
        pa = k - pb
        
        if A[pa - 1] > B[pb - 1]:
            return self.findKth(A, B[pb:], k - pb)
        elif A[pa - 1] < B[pb - 1]:
            return self.findKth(A[pa:], B, k - pa)
        else:
            return A[pa - 1]
            #二分删数组，也是跪了