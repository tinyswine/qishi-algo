#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:44:01 2019

@author: paul
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        if k==0:
            return 0
        
        if k*2>=len(prices):
            buy = float('-inf')
            sell = 0
            for price in prices:
                buy, sell = max(sell-price, buy), max(sell, buy+price)
            return sell
        
        buy = [float('-inf') for i in range(k)]
        sell = [0 for i in range(k)]

        for price in prices:
            for j in range(len(buy)):
                if j==0:
                    buy[j] = max(buy[j], -price)
                else:
                    buy[j] = max(buy[j], sell[j-1]-price)
                sell[j] = max(sell[j], buy[j]+price)
        return sell[-1]
    
if __name__ == "__main__":
    prices = [2,4,1]
    k = 2
    sol = Solution()
    print(sol.maxProfit(k, prices))