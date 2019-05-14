#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:05:53 2019

@author: paul
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.judge = True
        self.dfs(board, 0, 0)
        return self.judge
        
    def find_next_empty(self, x, y, board):
        for j in range(y+1, len(board)):
            if board[x][j]!='.':
                return x,j
        for i in range(x+1, len(board)):
            for j in range(len(board)):
                if board[i][j]!='.':
                    return i,j
        return -1,-1
    
    def dfs(self, board, x, y):
        next_x,next_y = self.find_next_empty(x, y, board)
        if next_x == -1:
            return
        
        if self.check(board, next_x, next_y, board[next_x][next_y]):
            self.dfs(board, next_x, next_y)
        else:
            self.judge = False
            return

        
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
    board = [[".","8","7","6","5","4","3","2","1"],
             ["2",".",".",".",".",".",".",".","."],
             ["3",".",".",".",".",".",".",".","."],
             ["4",".",".",".",".",".",".",".","."],
             ["5",".",".",".",".",".",".",".","."],
             ["6",".",".",".",".",".",".",".","."],
             ["7",".",".",".",".",".",".",".","."],
             ["8",".",".",".",".",".",".",".","."],
             ["9",".",".",".",".",".",".",".","."]]
    print(sol.isValidSudoku(board)) 