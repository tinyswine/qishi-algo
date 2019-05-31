#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:43:09 2019

@author: paul
"""

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        max_len = 0
        result_list = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
        for i in range(0,len(A)):
            for j in range(0,len(B)):
                if A[i]==B[j]:
                    result_list[i+1][j+1] = result_list[i][j]+1
                else:
                    result_list[i+1][j+1] = 0
                max_len = max(max_len, result_list[i+1][j+1])
        return max_len
    
if __name__ == "__main__":
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    sol = Solution()
    print(sol.findLength(A, B))