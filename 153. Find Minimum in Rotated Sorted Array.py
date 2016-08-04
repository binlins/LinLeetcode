#153. Find Minimum in Rotated Sorted Array
#-*- coding:utf-8 -*-
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #one    
        # tmp = 10000000
        # for x in nums:
        #     if tmp > x:
        #         tmp = x
        # return tmp        
    #two
        # nums.sort()
        # return nums[0]
    #three    
        low, hig = 0, len(nums)-1
        while low < hig:
            if (hig-low) == 1: 
                return min(nums[low], nums[hig])  

            if  nums[low] <= nums[hig]:
                return nums[low]
            mid = (hig - low) / 2 + low
            if nums[mid] < nums[hig]:
                hig = mid
            elif nums[low] < nums[mid]:
                low = mid
        return nums[low]        
        

#headache  leave for tomorrow
public class Solution {  
    // O(n) simple  
    public int findMin1(int[] num) {  
        int len = num.length;  
        if (len == 1) {  
            return num[0];  
        }  
          
        for (int i = 1; i < len; i++) {  
            if (num[i] < num[i-1]) {  
                return num[i];  
            }  
        }  
          
        return num[0];  
          
        // 尼玛，看成找中间数了  
        // if (len % 2 != 0) { //len is odd  
        //     return num[(begin+len/2)%len];  
        // } else {    //len is even  
        //     return (num[(begin+len/2-1)%len] + num[(begin+len/2)%len]) / 2;  
        // }  
    }  
      
      
    // O(lgn) not that good  
    public int findMin2(int[] num) {  
        int len = num.length;  
        if (len == 1) return num[0];  
          
        int left = 0, right = len-1;  
        while (left < right) {  
            if ((right-left) == 1) return Math.min(num[left], num[right]);  
              
            if (num[left] <= num[right]) return num[left];  
              
            int mid = (left + right) / 2;  
            if (num[mid] < num[right]) {  
                right = mid;  
            } else if (num[left] < num[mid]) {  
                left = mid;  
            }  
        }  
          
        return num[left];  
    }  
      
      
    // O(lgn) optimized iteratively  
    public int findMin3(int[] num) {  
        int len = num.length;  
        if (len == 1) return num[0];  
        int left = 0, right = len-1;  
        while (num[left] > num[right]) { // good idea  
            int mid = (left + right) / 2;  
            if (num[mid] > num[right]) {  
                left = mid + 1;  
            } else {  
                right = mid; // be careful, not mid-1, as num[mid] maybe the minimum  
            }  
        }  
        return num[left];  
    }  
      
      
    // O(lgn) optimized recursively  
    public int findMin(int[] num) {  
        return find(num, 0, num.length-1);  
    }  
      
    public int find(int[] num, int left, int right) {  
        if (num[left] <= num[right]) {  
            return num[left];  
        }  
        int mid = (left + right) / 2;  
        if (num[mid] > num[right]) {  
            return find(num, mid+1, right);  
        }  
        return find(num, left, mid);  
    }  
}  