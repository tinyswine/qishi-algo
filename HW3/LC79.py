#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:01:14 2019

@author: paul
"""

class Solution(object):
    
    def search(self, i, j, t):
        if self.board[i][j]!=self.word[t] or self.visited[(i,j)] == 1:
            return False
        
        if self.board[i][j]==self.word[t] and self.visited[(i,j)] == 0 and t == len(self.word)-1:
            return True
        
        self.visited[(i, j)] = 1
        
        up = (max(i-1, 0), j)
        down = (min(len(self.board)-1, i+1), j)
        left = (i, max(j-1,0))
        right = (i, min(len(self.board[0])-1, j+1))
        
        sign = self.search(up[0], up[1], t+1) or self.search(down[0], down[1], t+1) or self.search(left[0], left[1], t+1) or self.search(right[0], right[1], t+1)

        if not sign:
            self.visited[(i, j)] = 0
        return sign
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.visited = {}
        self.container = []
        
        self.board = board
        self.word = word
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.visited[(i,j)] = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(i,j,0):
                    return True
        return False
    
if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    sol = Solution()
    print(sol.exist(board, word))