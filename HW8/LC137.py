#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:19:17 2019

@author: paul
"""

class Solution:
    def singleNumber(self, nums):
        a, b = 0,0
        for num in nums:
            a = a^num&(~b);
            b = b^num&(~a);
        return a
    
if __name__ == "__main__":
    nums = [2,2,3,2]
    sol = Solution()
    print(sol.singleNumber(nums))