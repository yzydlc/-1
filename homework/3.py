# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:33:13 2021

@author: zyc
"""

def Pascal_triangle(k):
    list=[]
    list.append(1)
    
    if(k==0):
        print(1)
    m=1
    for i in range(1,k):
          m=m*i
    for i in range(1,k):
        n=1
        l=1
        for j in range(1,i+1):
            n=n*j
        for j in range(1,k-i):
            l=l*j
        list.append(int(m/(n*l)))
    return list
k=int(input("input k:"))
print(Pascal_triangle(k))
     
