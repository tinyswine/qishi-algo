#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:29:26 2019

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
    
    def maxthrough(self,node):
        if not node:
            return 0
        left_sum = max(self.maxthrough(node.left),0)
        right_sum = max(self.maxthrough(node.right),0)
        self.res = max(node.val+left_sum+right_sum, self.res)
        return max(left_sum, right_sum)+node.val
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')
        self.maxthrough(root)
        return self.res
    
if __name__ == "__main__":
    num_list = [-10,9,20,None,None,15,7]
    tree = Tree(num_list)
    sol = Solution()
    print(sol.maxPathSum(tree.root))