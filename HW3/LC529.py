#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:40:04 2019

@author: paul
"""

class Solution(object):
    
    def search(self, board, state):
        
        direction_list = [-1,0,1]
        
        count = 0
        for direction_i in direction_list:
            for direction_j in direction_list:
                if direction_i==0 and direction_j==0:
                    continue
                i, j = state[0]+direction_i, state[1]+direction_j
                if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                    continue
                if board[i][j] in ['M', 'X']:
                    count+=1
        
        if count:
            board[state[0]][state[1]] = str(count)
        else:
            board[state[0]][state[1]] = 'B'
            for direction_i in direction_list:
                for direction_j in direction_list:
                    if direction_i==0 and direction_j==0:
                        continue
                    i, j = state[0]+direction_i, state[1]+direction_j
                    if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                        continue
                    if board[i][j] == 'E':
                        board = self.search(board, [i,j])
        return board
            
    
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        return self.search(board, click)
        
if __name__ == "__main__":
        board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
        click = [3,0]
        sol = Solution()
        print(sol.updateBoard(board, click))