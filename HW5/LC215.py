#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:55:32 2019

@author: paul
"""

import heapq

class Heap:
    def __init__(self, k):
        self.k = k
        self.list = []
        
    def add(self, t):
        if len(self.list)<self.k:
            heapq.heappush(self.list, t)
        elif self.list[0]<t:
            heapq.heappop(self.list)
            heapq.heappush(self.list, t)
            
    def peek(self):
        return self.list[0]

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = Heap(k)
        for num in nums:
            heap.add(num)
        return heap.peek()
    
if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    sol = Solution()
    print(sol.findKthLargest(nums, k))