#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 20:12:42 2019

@author: siddharth
"""


import os
os.chdir('/home/siddharth/workspace-python/Python/Building TensorFlow API from Scratch/')

path  = os.getcwd()

import sys
sys.path.append(path)

class Session():
    
    def topology_sort(operation):
        ordering = [] 
        visited_nodes = set()
        
        def recursive_helper(node):
            if isinstance(node,Operation):
                for input_node in node.inputs:
                    if input_node not in visited_nodes:
                        recursive_helper(input_node)
                        
            visited_nodes.add(node)
            ordering.append(node)
            
        # recursive dfs
        recursive_helper(operation)
        
        return ordering