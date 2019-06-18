#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:04:42 2019

@author: paul
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result_list = [0]
        for i in range(1, num+1):
            k = i&1
            if k==1:
                result_list.append(result_list[-1]+1)
            else:
                result_list.append(result_list[i>>1])
        return result_list
    
if __name__ == "__main__":
    num = 2
    sol = Solution()
    print(sol.countBits(num))