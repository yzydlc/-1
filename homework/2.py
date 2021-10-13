# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:08:25 2021

@author: zyc
"""

import numpy as np
# 2.1 使用python中numpy模块进行随机数的生成
def Make_Matrices():
    rd=np.random.RandomState(888)
    matrix1=rd.randint(0,50,(5,10))
    matrix2=rd.randint(0,50,(10,5))
    print(matrix1)
    print(matrix2)
Make_Matrices()

# 2.2 
def Matrix_multip(matrix1,matrix2):
    M=[[[]for i in range(5)]for i in range(5)]
    for i in range(5):
       for j in range(5):
           for n in range(10):
             M[i][j]=matrix1[i][n]*matrix2[n][j]
    return M

     

