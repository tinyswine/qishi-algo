#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:41:11 2019

@author: paul
"""

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = float('-inf')
        sell = 0
        
        for price in prices:
            buy, sell = max(buy, sell-price), max(sell, buy+price-fee)
        return sell
    
if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    sol = Solution()
    print(sol.maxProfit(prices, fee))