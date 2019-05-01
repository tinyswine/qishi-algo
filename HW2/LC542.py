#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:15:49 2019

@author: paul
"""

class Solution:
    def updateMatrix(self, matrix):
        if not matrix:
            return matrix
        if not matrix[0]:
            return matrix
        n, m = len(matrix), len(matrix[0])
        zeros = [(i,j) for j in range(m) for i in range(n) if matrix[i][j]==0]
        
        sign = {}
        for element in zeros:
            sign[element] = 1
        
        count = 0
        while len(sign)!=n*m:
            count+=1
            tmp_list = []
            for element in zeros:
                i,j = element
                up = (max(i-1,0),j)
                down = (min(i+1,n-1),j)
                left = (i,max(j-1,0))
                right = (i, min(j+1, m-1))
                if sign.get(up, 0)!=1:
                    tmp_list.append(up)
                    sign[up] = 1
                    matrix[up[0]][up[1]] = count
                if sign.get(down, 0)!=1:
                    tmp_list.append(down)
                    sign[down] = 1
                    matrix[down[0]][down[1]] = count
                if sign.get(left, 0)!=1:
                    tmp_list.append(left)
                    sign[left] = 1
                    matrix[left[0]][left[1]] = count
                if sign.get(right, 0)!=1:
                    tmp_list.append(right)
                    sign[right] = 1
                    matrix[right[0]][right[1]] = count
            zeros = tmp_list
        return matrix
                
if __name__ == "__main__":
    matrix = [[0,0,0],[0,1,0],[0,0,0]]
    sol = Solution()
    print(sol.updateMatrix(matrix))             