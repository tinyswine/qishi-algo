#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:40:14 2019

@author: paul
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        profit1 = float('-inf')
        profit2 = 0
        profit3 = float('-inf')
        profit4 = 0
        for x in prices:
            profit1 = max(profit1, -x)
            profit2 = max(profit2, profit1+x)
            profit3 = max(profit3, profit2-x)
            profit4 = max(profit4, profit3+x)
        return profit4
    
if __name__ == "__main__":
    prices = [3,3,5,0,0,3,1,4]
    sol = Solution()
    print(sol.maxProfit(prices))