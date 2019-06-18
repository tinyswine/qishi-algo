#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:44:49 2019

@author: paul
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or m<<1<=n:
            return 0
        i = m+1
        while i<=n:
            m &= i
            i+=1
        return m
    
if __name__ == "__main__":
    m = 5
    n = 7
    sol = Solution() 
    print(sol.rangeBitwiseAnd(m,n))