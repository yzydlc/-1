# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def Print_values(int a,b,c):
    int a,b,c
    a=float(input())
    b=float(input())
    c=float(input())
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b>c:
            continue
        else:
            print(c,b,a)
            
Print_values()

    
    