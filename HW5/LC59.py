#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:37:52 2019

@author: paul
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        direction_list = [[0,1], [1,0], [0,-1], [-1,0]]
        
        matrix = [[0 for i in range(n)] for j in range(n)]
        
        count = 1
        
        x,y = 0,-1
        index = 0
        
        while count<=n*n:
            
            delta_x, delta_y = direction_list[index]
            
            x_new, y_new = x+delta_x,  y+delta_y
            
            if x_new<0 or x_new>=n or y_new<0 or y_new>=n:
                index+=1
                index = index % 4
                continue
    
            if matrix[x_new][y_new] != 0:
                index+=1
                index = index % 4
                continue
            
            x, y = x_new, y_new
            matrix[x][y] = count
            
            count+=1
            
        return matrix
    
if __name__ == "__main__":
    n = 3
    sol = Solution()
    print(sol.generateMatrix(n))