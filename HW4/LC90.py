#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:05:24 2019

@author: paul
"""

from copy import deepcopy

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dict_num = {}
        ans = []
        self.ret = []
        self.dfs(ans, dict_num, nums)
        return self.ret
        
    def dfs(self, ans, dict_num, nums):
        if len(nums)==0:
            self.ret.append(ans)
            return
        
        num = nums[0]
        if dict_num.get(num, 0)!=0:
            self.dfs(deepcopy(ans), dict_num, nums[1:])
        else:
            dict_num[num] = 1
            self.dfs(deepcopy(ans), deepcopy(dict_num), nums[1:])
            del dict_num[num]
            ans.append(num)
            self.dfs(deepcopy(ans), deepcopy(dict_num), nums[1:])
            ans.pop(-1)
        
        return

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2]
    print(sol.subsetsWithDup(nums)) 