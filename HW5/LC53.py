#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:59:17 2019

@author: paul
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = nums[0]
        local_sum = 0
        
        for num in nums:
            local_sum+=num
            high = max(local_sum - low, high)
            low = min(local_sum, low)
        return high
    
if __name__ == "__main__":
    list1 = [-2,-3]
    sol = Solution()
    print(sol.maxSubArray(list1))