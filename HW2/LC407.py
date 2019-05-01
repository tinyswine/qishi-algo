#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:19:51 2019

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

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap:
            return 0
        
        if not heightMap[0]:
            return 0
        
        heap = Heap()
        
        n = len(heightMap)
        m = len(heightMap[0])
        
        visited = {}
        
        i = 0
        for j in range(m):
            heap.push((heightMap[i][j], i, j))
            visited[(i,j)] = 1
            
        i = n-1
        for j in range(m):
            heap.push((heightMap[i][j], i, j))
            visited[(i,j)] = 1
            
        j = 0
        for i in range(1,n-1):
            heap.push((heightMap[i][j], i, j))
            visited[(i,j)] = 1
            
        j = m-1
        for i in range(1,n-1):
            heap.push((heightMap[i][j], i, j))
            visited[(i,j)] = 1
            
        area = 0
        height = 0
        while len(visited)<n*m:
            element = heap.pop()
            h, i, j = element
            
            height = max(height, h)
            
            up = (max(i-1,0), j)
            if visited.get(up, 0)!=1:
                area+=max(height-heightMap[up[0]][up[1]], 0)
                visited[up] = 1
                heap.push((heightMap[up[0]][up[1]], up[0], up[1]))
            
            down = (min(i+1,n-1), j)
            if visited.get(down, 0)!=1:
                area+=max(height-heightMap[down[0]][down[1]], 0)
                visited[down] = 1
                heap.push((heightMap[down[0]][down[1]], down[0], down[1]))
                
            left = (i, max(j-1,0))
            if visited.get(left, 0)!=1:
                area+=max(height-heightMap[left[0]][left[1]], 0)
                visited[left] = 1
                heap.push((heightMap[left[0]][left[1]], left[0], left[1]))
                
            right = (i, min(j+1,m-1))
            if visited.get(right, 0)!=1:
                area+=max(height-heightMap[right[0]][right[1]], 0)
                visited[right] = 1
                heap.push((heightMap[right[0]][right[1]], right[0], right[1]))
                
        return area
        

if __name__ == "__main__":
    heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    sol = Solution()
    print(sol.trapRainWater(heightMap))