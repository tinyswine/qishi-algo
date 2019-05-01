#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:34:28 2019

@author: paul
"""

class Solution:
    def findMinHeightTrees(self, n, edges):
        ###Try BFS from the leaves 
        adj = {}
        for i in range(n):
            adj[i] = {}
        for i,j in edges:
            adj[i][j] = 1
            adj[j][i] = 1
            
        sign = {}
            
        leaves = [i for i in range(n) if len(adj[i])==1]
        
        
        while True:
            for i in leaves:
                sign[i] = 1
            if len(sign)==n:
                return leaves
            for i in leaves:
                tmp_list = list(adj[i].keys())
                for j in tmp_list:
                    del adj[i][j]
                    del adj[j][i]
            if len(sign)==n-1:
                return [i for i in range(n) if sign.get(i,0)==0]
            leaves = [i for i in range(n) if len(adj[i])==1]
            
        
if __name__ == "__main__":
    n = 7
    edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
    sol = Solution()
    print(sol.findMinHeightTrees(n, edges))