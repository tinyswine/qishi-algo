#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:04:25 2019

@author: paul
"""

from copy import deepcopy

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        board = [['.' for i in range(n)] for j in range(n)]
        
        self.dfs(board, 0, n)
        
        return self.count
        
    def dfs(self, board, column, n):
        if column == n:
            self.count+=1
            return
        
        for i in range(n):
            if self.check(i, column, board, n):
                board[i][column] = 'Q'
                self.dfs(deepcopy(board), column+1, n)
                board[i][column] = '.'
        
        return
    
    def check(self, i, column, board, n):
        ##Upper diag
        for j in range(1,min(column,i)+1):
            if board[i-j][column-j] == 'Q':
                return False
        ##Lower diag
        for j in range(1, min(column, n-i-1)+1):
            if board[i+j][column-j] == 'Q':
                return False
        ##Left
        for j in range(1, column+1):
            if board[i][column-j] == 'Q':
                return False
        return True
        
if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.totalNQueens(n))
    