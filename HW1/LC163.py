#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:14:15 2019

@author: paul
"""

class Solution:
    def findMin(self, nums):
        if len(nums)==1:
            return nums[0]
        
        low = 0
        high = len(nums)-1
        while True:
            mid = int((low+high)/2)
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if low==len(nums)-1:
                return nums[0]
            if nums[mid]<nums[0]:
                high = mid-1
            else:
                low = mid+1
                
if __name__ == "__main__":
    nums = [3,4,5,1,2]
    sol = Solution()
    print(sol.findMin(nums))
    