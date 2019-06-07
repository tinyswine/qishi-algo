#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:53:11 2019

@author: paul
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        marked = {}
        for i in range(numCourses):
            marked[i] = 0
            
        pre_dict = {}
        post_dict = {}
        
        for pair in prerequisites:
            post, pre = pair
            value_list = post_dict.get(pre, [])
            if value_list:
                post_dict[pre].append(post)
            else:
                post_dict[pre] = [post]
            pre_dict[post] = pre_dict.get(post, 0)+1
        
        s_list = []
        
        for key in range(numCourses):
            if not pre_dict.get(key, 0):
                marked[key] = 1
                s_list.append(key)
                
        while s_list:
            w = s_list.pop(0)
            for v in post_dict.get(w, []):
                pre_dict[v] -= 1
                if marked[v] == 0 and (not pre_dict[v]):
                    marked[v] = 1
                    s_list.append(v)
        
        for i in range(numCourses):
            if marked[i] == 0:
                return False
        return True
        
                
            
        