#240. Search a 2D Matrix II
## -*- coding:utf-8 -*-

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for x in xrange(len(matrix[0])):
            res = self.bsearch(matrix, target, x)
            if res == True:
                return res
        return False        
        
    def bsearch(self, matrix, target, x):
        low, hig = 0, len(matrix)-1
        while low <= hig:
            mid = (low + hig) / 2
            if matrix[mid][x] < target:
                low = mid + 1
            elif matrix[mid][x] > target:     
                hig = mid - 1
            else:
                return True
        return False   
        # 遍历行，二分查找列

#two
    #右上角开始遍历
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0: return false
        n = len(matrix[0])
        
        i, j = 0, n-1
        while  i < m and j >= 0: 
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else: 
                i += 1
        
        return False