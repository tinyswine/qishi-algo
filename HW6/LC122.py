#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:39:50 2019

@author: paul
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('-inf')
        sell = 0
        
        for price in prices:
            buy, sell = max(buy, sell-price), max(buy+price, sell)
        return sell
    
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    sol = Solution()
    print(sol.maxProfit(prices))