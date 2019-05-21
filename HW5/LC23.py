#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:29:38 2019

@author: paul
"""


import heapq


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Heap:
    def __init__(self):
        self.list = []
    
    def push(self, val):
        heapq.heappush(self.list, val)
    
    def pop(self):
        return heapq.heappop(self.list)
    
    def empty(self):
        return len(self.list)==0
        
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if not lists:
            return None
        
        start = ListNode(0)
        cur = start
        
        heap = Heap()
        
        for i in range(len(lists)):
            if lists[i]:
                heap.push((lists[i].val, i))
        
        while not heap.empty():
            val, index = heap.pop()
            
            cur.next = ListNode(val)
            cur = cur.next
            lists[index] = lists[index].next
            if lists[index]:
                heap.push((lists[index].val, index))
        
        return start.next

if __name__ == "__main__":
   list1 = [[1,4,5],[1,3,4],[2,6]]
   list2 = []
   for tmp_list in list1:
       start = ListNode(0)
       cur = start
       for tmp in tmp_list:
           node = ListNode(tmp)
           cur.next = node
           cur = cur.next
       list2.append(start.next)
   sol = Solution()
   result = sol.mergeKLists(list2)
   while result:
       print(result.val)
       result = result.next