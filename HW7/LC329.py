#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 08:53:18 2019

@author: paul
"""

class Solution(object):
    
    def check(self, i,j):
        n, m = len(self.matrix), len(self.matrix[0])
        if (i>0) and (self.matrix[i-1][j]<self.matrix[i][j]):
            return False
        if (i<n-1) and (self.matrix[i+1][j]<self.matrix[i][j]):
            return False
        if (j>0) and (self.matrix[i][j-1]<self.matrix[i][j]):
            return False
        if (j<m-1) and (self.matrix[i][j+1]<self.matrix[i][j]):
            return False
        return True
    
    def DFS(self, i,j):
        n, m = len(self.matrix), len(self.matrix[0])
        if (i>0) and (self.matrix[i-1][j]>self.matrix[i][j]):
            if self.num[i-1][j]==0:
                self.num[i-1][j] = self.DFS(i-1,j)
            up = self.num[i-1][j]+1
        else:
            up = 1
        
        if (i<n-1) and (self.matrix[i+1][j]>self.matrix[i][j]):
            if self.num[i+1][j]==0:
                self.num[i+1][j] = self.DFS(i+1,j)
            down = self.num[i+1][j]+1
        else:
            down = 1
            
        if (j>0) and (self.matrix[i][j-1]>self.matrix[i][j]):
            if self.num[i][j-1]==0:
                self.num[i][j-1] = self.DFS(i,j-1)
            left = self.num[i][j-1]+1
        else:
            left = 1
            
        if (j<m-1) and (self.matrix[i][j+1]>self.matrix[i][j]):
            if self.num[i][j+1]==0:
                self.num[i][j+1] = self.DFS(i,j+1)
            right = self.num[i][j+1]+1
        else:
            right = 1
            
        self.num[i][j] = max(up, down, left, right)
            
        return self.num[i][j]
            
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.matrix = matrix
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        start_list = []
        
        self.num = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if self.check(i,j):
                    start_list.append([i,j])
        
        max_num = 0
        for start in start_list:
            max_num = max(self.DFS(start[0], start[1]), max_num)
            
        return max_num

if __name__ == "__main__":
    sol = Solution()    
    matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
    print(sol.longestIncreasingPath(matrix))