#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:48:55 2019

@author: paul
"""

class Solution:
    def get_island(self, A):
        island = []
        
        n = len(A)
        m = len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    break
            if A[i][j] == 1:
                break
                    
        x,y = i,j
        target_list = [(x,y)]
        A[x][y] = 2
        while target_list:
            island += target_list
            tmp_list = []
            for target in target_list:
                x, y = target
                up = (max(x-1,0), y)
                down = (min(x+1, n-1), y)
                left = (x, max(y-1,0))
                right = (x, min(y+1,m-1))
                if A[up[0]][up[1]]==1:
                    A[up[0]][up[1]] = 2
                    tmp_list.append(up)
                if A[down[0]][down[1]]==1:
                    A[down[0]][down[1]] = 2
                    tmp_list.append(down)
                if A[left[0]][left[1]]==1:
                    A[left[0]][left[1]] = 2
                    tmp_list.append(left)
                if A[right[0]][right[1]]==1:
                    A[right[0]][right[1]] = 2
                    tmp_list.append(right)
            target_list = tmp_list
        return island
    
    def shortestBridge(self, A):
        n = len(A)
        m = len(A[0])
        
        island1 = self.get_island(A)
        island2 = self.get_island(A)
        
        island2_dict = {}
        for element in island2:
            island2_dict[element] = 1
        
        target_list = island1
        count = 0
        
        while target_list:
            tmp_list = []
            for target in target_list:
                x, y = target
                up = (max(x-1,0), y)
                down = (min(x+1, n-1), y)
                left = (x, max(y-1,0))
                right = (x, min(y+1,m-1))
                
                if island2_dict.get(up, 0)==1:
                    return count
                if island2_dict.get(down, 0)==1:
                    return count
                if island2_dict.get(left, 0)==1:
                    return count
                if island2_dict.get(right, 0)==1:
                    return count
                
                if A[up[0]][up[1]]==0:
                    A[up[0]][up[1]] = 2
                    tmp_list.append(up)
                    
                if A[down[0]][down[1]]==0:
                    A[down[0]][down[1]] = 2
                    tmp_list.append(down)
                    
                if A[left[0]][left[1]]==0:
                    A[left[0]][left[1]] = 2
                    tmp_list.append(left)
                    
                if A[right[0]][right[1]]==0:
                    A[right[0]][right[1]] = 2
                    tmp_list.append(right)
                    
            count+=1
            target_list = tmp_list
        
            
                    
if __name__ == "__main__":
    A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    sol = Solution()
    print(sol.shortestBridge(A))                                 