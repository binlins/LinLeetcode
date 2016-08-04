#74.Search a 2D Matrix
# -*- coding:utf-8 -*-
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col, row = len(matrix), len(matrix[0])
        low, hig = 0, row * col - 1
        while low <= hig:
            mid = (low + hig) / 2
            num = matrix[mid/row][mid%row]
            if num > target:
                hig = mid - 1
            elif num < target:
                low = mid + 1
            else:
                return True
        return False        
        #so easy 二分，感觉智商上线