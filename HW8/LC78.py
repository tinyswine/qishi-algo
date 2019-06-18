#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:16:39 2019

@author: paul
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        set_num = 2**n
        result_list = []
        for i in range(set_num):
            tmp_list = []
            mul = 1
            for j in range(n):
                if mul&i>0:
                    tmp_list.append(nums[j])
                mul = mul<<1
            result_list.append(tmp_list)
        return result_list
    
if __name__ == "__main__":
    nums = [1,2,3]
    sol = Solution()
    print(sol.subsets(nums))