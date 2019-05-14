#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:57:41 2019

@author: paul
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.ret = []
        self.dfs(board, 0, -1)
        
    def find_next_empty(self, x, y, board):
        for j in range(y+1, len(board)):
            if board[x][j]=='.':
                return x,j
        for i in range(x+1, len(board)):
            for j in range(len(board)):
                if board[i][j]=='.':
                    return i,j
        return -1,-1
    
    def dfs(self, board, x, y):
        next_x,next_y = self.find_next_empty(x, y, board)
        
        if next_x == -1:
            return True
        
        for num in range(1, 10):
            if self.check(board, next_x, next_y, str(num)):
                board[next_x][next_y] = str(num)
                if self.dfs(board, next_x, next_y):
                    return True
                board[next_x][next_y] = '.'
        
    def check(self, board, x, y, num):
        ##row
        for j in range(len(board)):
            if board[x][j] == num:
                if y!=j:
                    return False
        ##col
        for i in range(len(board)):
            if board[i][y] == num:
                if x!=i:
                    return False
        ##square
        x_blo = int(x/3)
        y_blo = int(y/3)
        for i in range(3):
            for j in range(3):
                x_tmp, y_tmp = x_blo*3+i, y_blo*3+j
                if board[x_tmp][y_tmp] == num:
                    if x_tmp!=x or y_tmp!=y:
                        return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    board = [[".",".","9","7","4","8",".",".","."],
             ["7",".",".",".",".",".",".",".","."],
             [".","2",".","1",".","9",".",".","."],
             [".",".","7",".",".",".","2","4","."],
             [".","6","4",".","1",".","5","9","."],
             [".","9","8",".",".",".","3",".","."],
             [".",".",".","8",".","3",".","2","."],
             [".",".",".",".",".",".",".",".","6"],
             [".",".",".","2","7","5","9",".","."]]
    sol.solveSudoku(board)
    print(board) 