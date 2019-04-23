#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:16:29 2019

@author: paul
"""

class Solution:
    def sign(self, image, i, col):
        if col:
            for j in range(len(image)):
                if image[j][i]=='1':
                    return True
        else:
            for j in range(len(image[0])):
                if image[i][j]=='1':
                    return True
        return False
    
    def minArea(self, image, x, y):
        m = len(image)
        n = len(image[0])
        
        low = 0
        high = y
        while True:
            mid = int((low+high)/2)
            if self.sign(image, mid, True):
                if mid==0:
                    left = mid
                    break
                if not self.sign(image, mid-1, True):
                    left = mid
                    break
                else:
                    high = mid-1
            else:
                low = mid+1
   
        low = y
        high = n-1
        while True:
            mid = int((low+high)/2)
            if self.sign(image, mid, True):
                if mid==n-1:
                    right = mid
                    break
                if not self.sign(image, mid+1, True):
                    right = mid
                    break
                else:
                    low = mid+1
            else:
                high = mid-1
        
        low = 0
        high = x
        while True:
            mid = int((low+high)/2)
            if self.sign(image, mid, False):
                if mid==0:
                    down = mid
                    break
                if not self.sign(image, mid-1, False):
                    down = mid
                    break
                else:
                    high = mid-1
            else:
                low = mid+1
                
        low = x
        high = m-1
        while True:
            mid = int((low+high)/2)
            if self.sign(image, mid, False):
                if mid==m-1:
                    up = mid
                    break
                if not self.sign(image, mid+1, False):
                    up = mid
                    break
                else:
                    low = mid+1
            else:
                high = mid-1
                
        #print(down, up, left, right)
        return (up-down+1)*(right-left+1)
    
if __name__ == "__main__":
    image = [["0","1"]]
    x, y = 0, 1
    sol = Solution()
    print(sol.minArea(image, x, y))
                