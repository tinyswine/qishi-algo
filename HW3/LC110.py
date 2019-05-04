#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:04:59 2019

@author: paul
"""

class Tree:
    def __init__(self, tree_list):
        node_list = []
        for i in range(len(tree_list)):
            if tree_list[i]:
                node = TreeNode(tree_list[i])
                node_list.append(node)
                if i==0:
                    continue
                if (i-1) % 2 ==0:
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

class Solution(object):
    
    def cal_height(self, node):
        if not node:
            return 0
        else:
            return max(self.cal_height(node.left), self.cal_height(node.right))+1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not (self.isBalanced(root.left) and self.isBalanced(root.right)):
            return False
        if abs(self.cal_height(root.left) - self.cal_height(root.right))>1:
            return False
        return True
    
if __name__ == "__main__":
    num_list = [3,9,20,None,None,15,7]
    tree = Tree(num_list)
    sol = Solution()
    print(sol.isBalanced(tree.root))