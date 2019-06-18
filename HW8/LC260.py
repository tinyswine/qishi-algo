#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:35:45 2019

@author: paul
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        a = 0
        for i in nums:
            a ^= i
        
        num1 = 0
        t = 1
        while True: 
            if a&t>0 and num1==0:
                num1 = t
                break
            t = t<<1

        
        num1_list = []
        num2_list = []
        for i in nums:
            if i&num1>0:
                num1_list.append(i)
            else:
                num2_list.append(i)
        
        num1, num2 = 0,0
        for i in num1_list:
            num1^=i
        for i in num2_list:
            num2^=i
            
        return [num1, num2]
    
if __name__ == "__main__":
    nums = [0,1]
    sol = Solution()
    print(sol.singleNumber(nums))