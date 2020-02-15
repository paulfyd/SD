#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:59:59 2019

@author: paul
"""

from random import *
import math



## Random generation of the data

data=[]

for i in range(100):
    a=randint(0,3)
    b=randint(0,2)
    c=randint(0,1)
    l=[a,b,c]
    data.append(l)

# The 5 different possibilities for the split

split=[["A 0"],["A 0 1"],["A 0 1 2"],["B 0"],["B 0 1"]]


## Function that returns the GINIsplit of a set of data according to the attribute that we use to split the set of data into 2 sets
## It also returns the list l0 and l1, (l0 is composed of the data that verifies the condition, l1 the others)

def GINIsplit(data,attribute_split):
    l0=[]                       #list that verifies the condition "attribute_split"
    l1=[]                       #list that does not verify the condition "attribute_split"
    N_C0_l0=0                    #number of C=0 in the list l0 
    N_C0_l1=0                    #number of C=0 in the list l1 
    if attribute_split=="A 0":
        for i in data:
            if i[0]==0:          #if A=0, i append the data in l0 
                l0.append(i)
                if i[2]==0:
                    N_C0_l0+=1   #I count the number of time that C=0 in l0
            else : 
                l1.append(i)    #I do the same with l1
                if i[2]==0:
                    N_C0_l1+=1
        N_C1_l0=len(l0)-N_C0_l0
        N_C1_l1=len(l1)-N_C0_l1
    if attribute_split=="A 0 1":       #then we do the same for each possibility of attribute_split
        for i in data:
            if i[0]==0 or i[0]==1:
                l0.append(i)
                if i[2]==0:
                    N_C0_l0+=1
            else : 
                l1.append(i)
                if i[2]==0:
                    N_C0_l1+=1
        N_C1_l0=len(l0)-N_C0_l0
        N_C1_l1=len(l1)-N_C0_l1
    if attribute_split=="A 0 1":
        for i in data:
            if i[0]==0 or i[0]==1 or i[0]==2:
                l0.append(i)
                if i[2]==0:
                    N_C0_l0+=1
            else : 
                l1.append(i)
                if i[2]==0:
                    N_C0_l1+=1
        N_C1_l0=len(l0)-N_C0_l0
        N_C1_l1=len(l1)-N_C0_l1
    if attribute_split=="B 0":
        for i in data:
            if i[1]==0:
                l0.append(i)
                if i[2]==0:
                    N_C0_l0+=1
            else : 
                l1.append(i)
                if i[2]==0:
                    N_C0_l1+=1
        N_C1_l0=len(l0)-N_C0_l0
        N_C1_l1=len(l1)-N_C0_l1
    if attribute_split=="B 0 1":
        for i in data:
            if i[1]==0 or i[1]==1:
                l0.append(i)
                if i[2]==0:
                    N_C0_l0+=1
            else : 
                l1.append(i)
                if i[2]==0:
                    N_C0_l1+=1
        N_C1_l0=len(l0)-N_C0_l0
        N_C1_l1=len(l1)-N_C0_l1
    if len(l0)==0 or len(l1)==0:
        return 0,l0,l1
    s=(float(len(l0))/len(data))*(1-(float(N_C0_l0)/len(l0))**2-(float(N_C1_l0)/len(l0))**2)
    s2=(float(len(l1))/len(data))*(1-(float(N_C0_l1)/len(l1))**2-(float(N_C1_l1)/len(l1))**2)
    return s+s2,l0,l1
  
    
## We create a dictionnary that we will update at each iteration and that will be very practical for the final print
res={}


## Recursive function that fills the dictionnary for an iteration and that call 2 new iterations for the two sons of the node

def Iteration(data,split_possibles,niveau,minNum):
    possible=True
    C0=0
    for j in data :               
        if j[2]==0:
            C0+=1
    if C0==0 or C0==len(data):    # if there are only C=0 or C=1 in our data, we do nothing
        possible=False 
        print("arret1")
    if len(split_possibles)==0:   #if all the possibilies of split have been used, we do nothing
        possible=False
        print("arret2")
    if len(data)<minNum:          #if the number of data in our set is inferior to minNum, we do nothing
        possible=False
        print("arret3")
    if possible==True:           
        maxGINI=GINIsplit(data,split_possibles[0][0])[0]
        split_retenu=split_possibles[0]
        for i in split_possibles:       #we calculate the max of the GINIsplit for the remaining split_possities
            a=GINIsplit(data,i[0])[0]
            if a>maxGINI:
                maxGINI=a
                split_retenu=i
        n_split_possibles=[]
        for i in split_possibles:
            if i!=split_retenu:        #we delete the split_possibility that we just used for the future
                n_split_possibles.append(i)
        res[niveau-1]=(split_retenu[0],GINIsplit(data,split_retenu[0])[0])   #we append our result to our dictionnary
        data1=GINI(data,split_retenu[0])[1]                                 #we do again our function for the two sons
        data2=GINI(data,split_retenu[0])[2]
        if maxGINI!=0.0:
            Iteration(data1,n_split_possibles,2*niveau,minNum)
            Iteration(data2,n_split_possibles,2*niveau+1,minNum)
  




def BuldingDecisionTree(data,minNum):  
    Iteration(data,split,1,minNum)
    for i in range(0,50):
        if i==0:
            print("Root\nLevel 1\n"+"Feature "+res[0][0]+"\n"+"GINI"+str(res[0][1]))
        else :
            if 2*i in list(res.keys()):
                if i==1:
                     print("Intermediate\nLevel 2"+"\n"+"Feature "+res[i][0]+"\n"+"GINI "+str(res[i][1]))
                else:
                    print("Intermediate\nLevel "+str(int(math.ceil(math.log(i,2)+1)))+"\n"+"Feature "+res[i][0]+"\n"+"GINI "+str(res[i][1]))
            else:
                if i in list(res.keys()):
                    print("Leaf\nLevel "+str(int(math.ceil(math.log(i,2)+1)))+"\n"+"GINI "+str(res[i][1]))
                
 



