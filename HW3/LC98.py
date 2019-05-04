#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:11:18 2019

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
    
    def findmostleft(self, node):
        val = float('inf')
        while node:
            val = node.val
            node = node.left
        return val
    
    def findmostright(self, node):
        val = float('-inf')
        while node:
            val = node.val
            node = node.right
        return val
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        sign = self.isValidBST(root.left) and self.isValidBST(root.right)
        
        if sign:
            left_max = self.findmostright(root.left)
            right_min = self.findmostleft(root.right)
            return root.val>left_max and root.val<right_min
        
        return False
        
if __name__ == "__main__":
    num_list = [5,1,4,None,None,3,6]
    tree = Tree(num_list)
    sol = Solution()
    print(sol.isValidBST(tree.root))