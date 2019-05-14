#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:20:15 2019

@author: paul
"""

from copy import deepcopy

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ret = []
        ans = [] 
        self.dfs(ans, k, n, 1, 0)
        return self.ret
        
    def dfs(self, ans, k, n, i, sum_ans):
        if len(ans)==k:
            if sum_ans==n:
                self.ret.append(ans)
            return
        
        if i>9:
            return
        
        if i+sum_ans<=n:
            ans.append(i)
            sum_ans+=i
            self.dfs(deepcopy(ans), k, n, i+1, sum_ans)
            ans.pop(-1)
            sum_ans-=i
            self.dfs(deepcopy(ans), k, n, i+1, sum_ans)
        else:
            return
        
if __name__ == "__main__":
    sol = Solution()
    k,n = 3, 7
    print(sol.combinationSum3(k, n)) 