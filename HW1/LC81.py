#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:52:32 2019

@author: paul
"""

class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        
        if len(nums)==1:
            start = 0
        
        while True:
            mid = int((low+high)/2)
            if nums[mid]<nums[mid-1]:
                start = mid
                break
            if mid == len(nums)-1:
                start = 0
                break
            if nums[mid]>=nums[0]:
                low = mid+1
            elif nums[mid]<nums[0]:
                high = mid-1
        
        low = 0
        high = len(nums)-1
        while True:
            mid = int((low+high)/2)
            index = (mid+start) % len(nums)
            
            if nums[index]==target:
                return True
            if low>=high:
                return False
            
            if nums[index]<target:
                low = mid+1
            elif nums[index]>target:
                high = mid-1
                
if __name__ == "__main__":
    nums = [2,5,6,0,0,1,2]
    target = 0
    sol = Solution()
    print(sol.search(nums, target))