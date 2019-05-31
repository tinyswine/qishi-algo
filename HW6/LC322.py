#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 10:42:05 2019

@author: paul
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [-1 for i in range(amount+1)]
        res[0] = 0
        for target in range(1, len(res)):
            for coin in coins:
                if target-coin<0:
                    continue
                if res[target-coin] > -1:
                    if res[target]==-1:
                        res[target] = res[target-coin]+1
                    else:
                        res[target] = min(res[target], res[target-coin]+1)
        return res[-1]
    
if __name__ == "__main__":
    coins = [1, 2, 5] 
    amount = 11
    sol = Solution()
    print(sol.coinChange(coins, amount))