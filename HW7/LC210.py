#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:07:00 2019

@author: paul
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        pre_dict = {}
        post_dict = {}
        marked = {}
        
        for value in prerequisites:
            post, pre = value
            if not post_dict.get(pre, []):
                post_dict[pre] = [post]
            else:
                post_dict[pre].append(post)
            pre_dict[post] = pre_dict.get(post, 0)+1
        
        s_list = []
        for num in range(numCourses):
            if not pre_dict.get(num, 0):
                s_list.append(num)
                marked[num] = 1
            else:
                marked[num] = 0
        
        result_list = []
        while s_list:
            w = s_list.pop(0)
            result_list.append(w)
            for v in post_dict.get(w, []):
                pre_dict[v] -= 1
                if marked[v] == 0 and (not pre_dict[v]):
                    marked[v] = 1
                    s_list.append(v)
        
        for num in range(numCourses):
            if marked[num] == 0:
                return []
        return result_list