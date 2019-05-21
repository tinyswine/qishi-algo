#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:35:37 2019

@author: paul
"""

class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        left = min(nums)
        right = max(nums)
        while True:
            mid = (left+right)/2.0
            if right-left<0.0001:
                return mid
            if self.check_avg(nums, mid, k):
                left = mid
            else:
                right = mid
        
    def check_avg(self, nums, avg, k):
        local_sum1 = 0
        local_sum2 = 0
        low = 0
        for i in range(k):
            local_sum2 += (nums[i]-avg)
        high = local_sum2
        
            
        for i in range(len(nums)-k):
            local_sum1 += (nums[i]-avg)
            local_sum2 += (nums[i+k]-avg)
            low = min(low, local_sum1)
            high = max(high, local_sum2-low)
        return high>=0
    
if __name__ == "__main__":
    nums = [10,201,11,12,13,13,202,77,89,101,-9,-10,-1,101,1001,11,203]
    k = 11
    sol = Solution()
    print(sol.maxAverage(nums, k))