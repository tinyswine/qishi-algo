#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:45:01 2019

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
        cooldown = 0
        
        for price in prices:
            buy, sell, cooldown = max(sell-price, buy), max(cooldown, sell), buy+price
        return max(sell, cooldown)
    
if __name__ == "__main__":
    prices = [1,2,3,0,2]
    sol = Solution()
    print(sol.maxProfit(prices))