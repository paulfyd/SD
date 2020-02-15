#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:03:29 2019

@author: paul
"""


split=[["a0"],["a0a1"],["a0a1a2"],["b0"],["b0b1"],["c0"]]
#data = liste sur laquelle on travaille, qu'on va devoir créer 
data=[[[1,1,0],[2,2,0],[0,0,0],[3,2,1],[0,0,0],[1,2,1]]]

def GINI(l,le_split):
    n=len(l)
    N0=0
    N1=0
    l0=[]
    l1=[]
    if le_split=="a0":
        for i in l:
            if i[0]==0:
                N0+=1
                l0.append(i)
            else : 
                l1.append(i)
        N1=n-N0
    if le_split=="a0a1":
        for i in l: 
            if i[0]==0 or i[0]==1:
                N0+=1
                l0.append(i)
            else:
                l1.append(i)
        N1=n-N0
    if le_split=="a0a1a2":
        for i in l: 
            if i[0]==0 or i[0]==1 or i[0]==2:
                N0+=1
                l0.append(i)
            else: 
                l1.append(i)
        N1=n-N0
    if le_split=="b0":
        for i in l: 
            if i[1]==0:
                N0+=1
                l0.append(i)
            else: 
                l1.append(i)
        N1=n-N0
    if le_split=="b0b1":
        for i in l: 
            if i[1]==0 or i[1]==1:
                N0+=1
                l0.append(i)
            else:
                l1.append(i)
        N1=n-N0
    if le_split=="c0":
        for i in l: 
            if i[2]==0:
                N0+=1
                l0.append(i)
            else:
                l1.append(i)
        N1=n-N0
    return (1-((float(N0)/n)**2)-((float(N1))/n)**2,l0,l1)




def min(l):
    res=l[0]
    ind=0
    for i in range(len(l)):
        if l[i]<res and l[i]!=0:
            res=l[i]
            ind=i
    return res,ind




while(len(split)!=1):
    n=len(split)
    tableau_des_mins=[]          #deuxième indice pour savoir quel split est concerné 
    for j in range(len(data)):          # plusieurs listes dans data 
        l=[0]*len(split)              # tableau des GINI concernant la liste data[j]
        for i in range (len(split)):  
            l[i]=GINI(data[j],split[i][0])[0]
            print(GINI(data[j],split[i][0]))
        a=min(l)                        #min de la liste data[j], et le split concerné 
        tableau_des_mins.append([a,j])
        print tableau_des_mins #on garde en mémoire aussi la liste j, qu'on devra splité 
    min_global=tableau_des_mins[0]      
    for i in range(len(tableau_des_mins)):
        if tableau_des_mins[i][0][0]<min_global and tableau_des_mins[i][0][0]!=0:
            min_global=tableau_des_mins[i]   #le min global à l'étape correspondante, on va donc faire le split sur celui-là; min_global=[[le GINI min, le split],l'indice j de la liste data]
     #on supprime le split que l'on a fait 
    print(min_global)
    print split[min_global[0][1]]
    data.append(GINI(data[min_global[1]],split[min_global[0][1]][0])[1])
    data.append(GINI(data[min_global[1]],split[min_global[0][1]][0])[2])
    del data[min_global[1]]
    del split[min_global[0][1]]
    print(data)





    
    
