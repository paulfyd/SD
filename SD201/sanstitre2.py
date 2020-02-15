#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:48:55 2019

@author: paul
"""

res2={}
import math

def entropy(N1,N2): 
    N=N1+N2
    if N==0: 
        return 0
    #print N1,N2
    if N1==0:
        return -(float(N2)/N)*math.log(float(N2)/N,2)
    if N2==0:
        return -(float(N1)/N)*math.log(float(N1)/N,2)
    return -(float(N2)/N)*math.log(float(N2)/N,2)-(float(N1)/N)*math.log(float(N1)/N,2)

def Gain2(data,attribute_split):
    l0=[]                       #list that verifies the condition "attribute_split"
    l1=[]                       #list that does not verify the condition "attribute_split"
    N_C0_l0=0                    #number of C=0 in the list l0 
    N_C0_l1=0                    #number of C=0 in the list l1 
    if attribute_split=="A 0":
        for i in data:
            if i[0]==0:          #if A=0, we append the data in l0 
                l0.append(i)
                if i[2]==0:
                    N_C0_l0+=1   #we count the number of time that C=0 in l0
            else : 
                l1.append(i)    #we do the same with l1
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
    if attribute_split=="A 0 1 2":
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
        print(l0,l1)
        N_C1_l0=len(l0)-N_C0_l0
        N_C1_l1=len(l1)-N_C0_l1
    N_C0_data=N_C0_l1+N_C0_l0
    N_C1_data=N_C1_l1+N_C1_l0
    return entropy(N_C0_data,N_C1_data)-(float(len(l0))/len(data))*entropy(N_C0_l0,N_C1_l0)-(float(len(l1))/len(data))*entropy(N_C0_l1,N_C1_l1),l0,l1


def Iteration(data,split_possibles,niveau,minNum):
    possible=True
    compteur_C0=0
    for i in data:
        if i[2]==0:
            compteur_C0+=1
    compteur_C1=len(data)-compteur_C0
    if len(split_possibles)==0 or (compteur_C0==0) or (compteur_C0==len(data)):   #if all the possibilies of split have been used, we do nothing
        possible=False
        res2[niveau]=1-(float(compteur_C0)/len(data))**2-(float(compteur_C1)/len(data))**2
        print("arret2")
    #if len(data)<=minNum:          #if the number of data in our set is inferior to minNum, we do nothing
        #possible=False
        #print("arret3")
    if possible==True:           
        maxGain=Gain2(data,split_possibles[0][0])[0]
        split_retenu=split_possibles[0]
        for i in split_possibles:       #we calculate the max of the GINIsplit for the remaining split_possities
            a=Gain2(data,i[0])[0]
            print(a,i)
            if a>maxGain:
                maxGain=a
                split_retenu=i
        n_split_possibles=[]
        for i in split_possibles:
            if i[0][0]!=split_retenu[0][0]:        #we delete the split_possibility that we just used for the future
                n_split_possibles.append(i)
        res2[niveau]=(split_retenu[0],Gain2(data,split_retenu[0])[0])   #we append our result to our dictionnary
        data1=Gain2(data,split_retenu[0])[1]                                 #we do again our function for the two sons
        data2=Gain2(data,split_retenu[0])[2]
        if len(data1)>=minNum:
            Iteration(data1,n_split_possibles,2*niveau,minNum)
        if len(data2)>=minNum:
            Iteration(data2,n_split_possibles,2*niveau+1,minNum)
            
split=[["A 0"],["A 0 1"],["A 0 1 2"],["B 0"],["B 0 1"]]

def BuldingDecisionTree2(data,minNum):  
    Iteration(data,split,1,minNum)
    for i in range(1,10):
        if i==1:
            print("Root\nLevel 1\n"+"Feature "+res2[1][0]+"\n"+"Gain "+str(res2[1][1]))
        else :
            if 2*i in list(res2.keys()) or 2*i+1 in list(res2.keys()):
                    print("Intermediate\nLevel "+str(int(math.log(i,2))+1)+"\n"+"Feature "+str(res2[i][0])+"\nGain "+str(res2[i][1]))
            else:
                if i in list(res2.keys()):
                    print("Leaf\nLevel "+str(int(math.log(i,2))+1)+"\nGINI"+str(res2[i]))


