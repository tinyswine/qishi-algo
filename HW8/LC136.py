#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:17:22 2019

@author: paul
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            count ^= i
        return count
    
if __name__ == "__main__":
    nums = [2,2,1]
    sol = Solution()
    print(sol.singleNumber(nums))