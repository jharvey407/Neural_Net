# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 03:58:12 2025

@author: James
"""


# Inputs
inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2

#Calculate
output = (inputs[0]*weights[0] +
          inputs[1]*weights[1] +
          inputs[2]*weights[2] + bias)

#Output
print(output)
