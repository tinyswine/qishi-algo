#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:46:19 2019

@author: paul
"""

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        
        if not matrix[0]:
            return False
        
        low = 0
        high = len(matrix)-1
        while low+1<high:
            mid = int((low+high)/2)
            if matrix[mid][0]<target:
                low = mid
            elif matrix[mid][0]>target:
                high = mid-1
            else:
                return True
        if matrix[high][-1]<target:
            return False
        elif matrix[high][0]<=target:
            row = high
        elif matrix[low][0]<=target:
            row = low
        else:
            return False
        
        low = 0
        high = len(matrix[0])-1
        while low<high:
            mid = int((low+high)/2)
            if matrix[row][mid]<target:
                low = mid+1
            elif matrix[row][mid]>target:
                high = mid-1
            else:
                return True
        if matrix[row][low]==target:
            return True
        return False
            
if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 3
    sol = Solution()
    print(sol.searchMatrix(matrix,target))