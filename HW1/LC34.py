# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution:
    def searchRange(self, nums, target):
        
        if not nums:
            return -1,-1
        
        low = 0
        high = len(nums)-1
        while low+1<high:
            mid = int((high-low)/2+low)
            if nums[mid]<target:
                low = mid+1
            elif nums[mid]>=target:
                high = mid
        if nums[low] == target:
            first = low
        elif nums[high] == target:
            first = high
        else:
            first = -1
    
        low = 0
        high = len(nums)-1
        while low+1<high:
            mid = int((high-low)/2+low)
            if nums[mid]<=target:
                low = mid
            elif nums[mid]>target:
                high = mid-1
        if nums[high] == target:
            last = high
        elif nums[low] == target:
            last = low
        else:
            last = -1
        
        return first, last
    
    
if __name__ == "__main__":
    nums = [0,1,2,2,3,3,3,5,6]
    target = 3
    sol = Solution()
    print(sol.searchRange(nums, target))