#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:37:08 2019

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
    
    def preorder(self, node):
        if node:
            self.val_list.append(node.val)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.val_list = []
        self.root = root
        self.preorder(root)
        return self.val_list
    
if __name__ == "__main__":
    num_list = [1,None,2,3]
    tree = Tree(num_list)
    sol = Solution()
    print(sol.preorderTraversal(tree.root))