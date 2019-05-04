#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:13:42 2019

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
         
     def inorder(self, node):
         if node:
             self.val_list.append(node.val)
             self.inorder(node.left)
             self.inorder(node.right)
         else:
             self.val_list.append(None)
         
     def print_tree(self):
         self.val_list = []
         self.inorder(self)
         print(self.val_list[:-2])

class Solution(object):
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.val_list.append(node.val)
            self.inorder(node.right)
    
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val_list = []
        self.inorder(root)
        
        root = TreeNode(self.val_list[0])
        cur = root
        
        for val in self.val_list[1:]:
            cur.right = TreeNode(val)
            cur = cur.right
            
        return root
        
if __name__ == "__main__":
    num_list = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    tree = Tree(num_list)
    sol = Solution()
    root = sol.increasingBST(tree.root)
    root.print_tree()