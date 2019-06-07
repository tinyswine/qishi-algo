#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:29:47 2019

@author: paul
"""

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        
        n = len(org)
        
        pre_dict = {}
        post_dict = {}
        marked = {}
        
        for seq in seqs:
            if len(seq) == 0:
                break
            elif len(seq) == 1:
                pre = seq[0]
                post_dict[pre] = []
            else:
                for i in range(len(seq)-1):
                    pre, post = seq[i], seq[i+1]
                    if post_dict.get(pre, []):
                        post_dict[pre].append(post)
                    else:
                        post_dict[pre] = [post]
                    pre_dict[post] = pre_dict.get(post, 0)+1
           
        
        s_list = []  
        for num in post_dict:
            if pre_dict.get(num, 0) == 0:
                s_list.append(num)
                marked[num] = 1
            else:
                marked[num] = 0
             
        result_list = []   
        while s_list:
            if len(s_list)>1:
                return False
            
            w = s_list.pop(0)
            result_list.append(w)
            if w!=org[len(result_list)-1]:
                return False
            for v in post_dict.get(w, []):
                pre_dict[v] -= 1
                if marked.get(v, 0)==0 and pre_dict[v]==0:
                    s_list.append(v)
                    marked[v] = 1

        
        
        if len(org)!=len(result_list):
            return False
            
        return True