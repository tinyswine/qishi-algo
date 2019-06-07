#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 00:06:47 2019

@author: paul
"""

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        
        pre_dict = {}
        post_dict = {}
        marked = {}
        showed = {}
        
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            for j in range(len(word2)):
                w1, w2 = word1[j], word2[j]
                if w1!=w2:
                    if post_dict.get(w1, []):
                        post_dict[w1].append(w2)
                    else:
                        post_dict[w1] = [w2]
                    pre_dict[w2] = pre_dict.get(w2, 0)+1
                    break
            for j in range(len(word1)):
                showed[word1[j]] = 1
            for j in range(len(word2)):
                showed[word2[j]] = 1
          
        param_list = []      
        for key in showed:
            if post_dict.get(key, [])==[] and pre_dict.get(key, 0)==0:
                param_list.append(key)
        param_list.sort()
        count = 0
        
                
        result_list = []
        s_list = []
        for w in post_dict:
            if pre_dict.get(w, 0) == 0:
                s_list.append(w)
                marked[w] = 1
        
        while s_list:
            w = s_list.pop(0)
            
            if count<len(param_list):
                while param_list[count]<w:
                    result_list.append(param_list[count])
                    count+=1
                    if count>=len(param_list):
                        break
                
            result_list.append(w)
            for v in post_dict.get(w, []):
                pre_dict[v] -= 1
                if marked.get(v, 0)==0 and pre_dict[v]==0:
                    s_list.append(v)
                    marked[v] = 1
                
        if count<len(param_list):
            result_list+=param_list[count:]
            
        if len(result_list)<len(showed):
            return ""
            
        return "".join(result_list)