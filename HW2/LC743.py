#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:53:32 2019

@author: paul
"""

import heapq

class Heap:
    def __init__(self):
        self.list = []
        
    def push(self, element):
        heapq.heappush(self.list, element)

    def pop(self):
        return heapq.heappop(self.list)
    
    def deduct(self, x):
        for i in range(len(self.list)):
            w,u,v = self.list[i]
            self.list[i] = (max(w-x,0),u,v)
    
    def empty(self):
        return not len(self.list)
        
class Solution:
    def networkDelayTime(self, times, N, K):
        
        heap = Heap()
        
        visited = {}
        
        path_dict = {}
        for time in times:
            u,v,w = time
            path_dict[u] = path_dict.get(u, []) + [time]
            
        visited[K] = 1
        for path in path_dict.get(K, []):
            u,v,w = path
            heap.push((w,u,v))
        
        total_time = 0
        while len(visited)<N:
            if heap.empty():
                return -1
            shortest_path = heap.pop()
            w,u,v = shortest_path
            if visited.get(v,0)==1:
                continue
            total_time+=w
            heap.deduct(w)
            if visited.get(v,0)!=1:
                for path in path_dict.get(v, []):
                    u1,v1,w1 = path
                    heap.push((w1,u1,v1))
                visited[v] = 1
        return total_time
        
if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    N = 4
    K = 2
    sol = Solution()
    print(sol.networkDelayTime(times, N, K))
        