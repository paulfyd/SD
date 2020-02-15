#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:10:01 2019

@author: paul
"""

import numpy as np




def product(d,v): #Return the product of a sparse matrice represented by a dictionnary d and a vector v 
    n=len(v)
    res=np.zeros(n)
    for i in range(n):
        l=d[i+1]
        for x in l:
            res[x-1]+=(1./len(l))*v[i]
    return res

def distance(r1,r2): #Return the norm1 of the vector r1-r2 (to see the difference between r1 and r2)
    res=0
    n=len(r1)
    for i in range(n):
        res+=abs(r1[i]-r2[i])
    return res

def PageRank(fichier,Beta,ecart): 
    x= np.array([[1.0],[1.0],[1.0],[1.0],[1.0],[1.0]])
    x=x/6
    p= np.array([1.0,1.0,1.0,1.0,1.0,1.0])
    p=p/6
    p=(1-Beta)*p
    f = open(fichier,'r')
    d={}
    for line in f:
        u,v= [int(x) for x in line.split()]
        if u in d:
            d[u].append(v)
        else:
            d[u]=[v]
    
    while distance(x,Beta*product(d,x)+p)>0.001:
        print(distance(x,product(d,x)))
        x=product(d,x)
    return x 
    




d=read2('/home/paul/Bureau/graphe')


    
"""Second case : beta = 0.8"""


y= np.array([[1.0],[1.0],[1.0],[1.0],[1.0],[1.0]])
y=y/6

p= np.array([1.0,1.0,1.0,1.0,1.0,1.0])
p=p/6
p=0.2*p

while distance(y,0.8*product(d,y)+p)>0.001:
    y=0.8*product(d,y)+p
    print("y=",y)
    




