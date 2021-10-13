# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 19:24:37 2021

@author: zyc
"""
import random
def Least_moves(x):
    #x=round(random.random()*100)
    i=0
    #对x=2和3的情况直接输出所需步骤
    if(x==2):
        i=1
        x=1
    if(x==3):
        i=2
        x=1
    #处理x>3的情况
    while((x>3)):#循环直到x<=3,循环中对偶数直接进行/2步骤+1，奇数则/2再向下取整（或者说先-1再/2），步骤+2
        m=x%2
        if(m==1):
            i=i+2
            x=int(x/2)
        else:
            i=i+1
            x=x/2
    #最后对循环结束的随机数处理，如果等于2，步骤+1，如果等于3，步骤+2
    if(x==2):
        i=i+1
    if(x==3):
        i=i+2
    return i
x=round(random.random()*100)
print("rondom number is:",x)
print("the least moves is:",Least_moves(x))
        