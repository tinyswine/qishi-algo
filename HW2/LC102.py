#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 12:09:07 2019

@author: paul
"""

class Tree:
    def __init__(self, tree_list):
        node_list = []
        for i in range(len(tree_list)):
            if tree_list[i]:
                node = TreeNode(tree_list[i])
                node_list.append(node)
                if i-1 % 2 ==0:
                    node_list[int((i-1)/2)].left = node
                else:
                    node_list[int((i-2)/2)].right = node
        if node_list:
            self.root = node_list[0]
        else:
            self.root = None
                

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from collections import deque

class Solution:
    def levelOrder(self, root):
        if root == None:
            return []
        q = deque([root])
        result_list = []
        while q:
            size = len(q)
            tmp_list = []
            for i in range(size):
                element = q.popleft()
                tmp_list.append(element.val)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            result_list.append(tmp_list)
        return result_list
    
if __name__ == "__main__":
    tree_list = [3,9,20,None,None,15,7]
    tree = Tree(tree_list)
    sol = Solution()
    print(sol.levelOrder(tree.root))