#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:26:00 2019

@author: paul
"""

class Solution:
    def search(self, nums, target) -> int:
        low = 0
        high = len(nums)-1
        while True:
            mid = int((low+high)/2)
            if nums[mid] == target:
                return mid
            if low>=high:
                return -1
            if nums[mid]>target:
                high = mid-1
            elif nums[mid]<target:
                low = mid+1
                
if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    sol = Solution()
    print(sol.search(nums, target))