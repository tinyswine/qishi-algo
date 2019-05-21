#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:11:04 2019

@author: paul
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix:
            return []
        
        direction_list = [[0,1], [1,0], [0,-1], [-1,0]]
        
        n, m = len(matrix), len(matrix[0])
        count = 0
        
        x,y = 0,-1
        index = 0
        
        result_list = []
        
        while count<n*m:
            
            delta_x, delta_y = direction_list[index]
            
            x_new, y_new = x+delta_x,  y+delta_y
            
            if x_new<0 or x_new>=n or y_new<0 or y_new>=m:
                index+=1
                index = index % 4
                continue
    
            if matrix[x_new][y_new] == None:
                index+=1
                index = index % 4
                continue
            
            x, y = x_new, y_new
            result_list.append(matrix[x][y])
            matrix[x][y] = None
            
            count+=1
            
        return result_list
    
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    print(sol.spiralOrder(matrix))