#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:58:49 2019

@author: paul
"""

class Solution:
    def findPeakElement(self, nums):
        
        if len(nums)==1:
            return 0
        
        low = 0
        high = len(nums)-1
        while True:
            mid = int((low+high)/2)
            if mid == 0:
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    low = mid + 1
            elif mid == len(nums)-1:
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    high = mid - 1
            else:
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return mid
                elif nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
                    low = mid+1
                elif nums[mid]<nums[mid-1] and nums[mid]>nums[mid+1]:
                    high = mid-1
                elif nums[mid]>nums[mid-1] and nums[mid]<nums[mid+1]:
                    low = mid+1
                    
if __name__ == "__main__":
    nums = [1,2,3,1]
    sol = Solution()
    print(sol.findPeakElement(nums))
    