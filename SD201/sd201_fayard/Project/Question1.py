#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:48:55 2019

@author: paul
"""



import math

def entropy(N1,N2): 
    N=N1+N2
    if N==0: 
        return 0
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
        N_C1_l0=len(l0)-N_C0_l0
        N_C1_l1=len(l1)-N_C0_l1
    N_C0_data=N_C0_l1+N_C0_l0
    N_C1_data=N_C1_l1+N_C1_l0
    return entropy(N_C0_data,N_C1_data)-(float(len(l0))/len(data))*entropy(N_C0_l0,N_C1_l0)-(float(len(l1))/len(data))*entropy(N_C0_l1,N_C1_l1),l0,l1


def Iteration(data,split_possibles,niveau,minNum,dico):     #update the global dictionnary dico, that represents our tree
    possible=True
    compteur_C0=0
    for i in data:
        if i[2]==0:
            compteur_C0+=1
    compteur_C1=len(data)-compteur_C0                 #we count if C=0 or C=1 is more present in our data, and we keep this info on the dico
    if len(split_possibles)==0 or (compteur_C0==0) or (compteur_C0==len(data)) or len(data)<minNum:     #stop conditions
        possible=False
        if compteur_C0>compteur_C1:
            dico[niveau]=("leaf"," ",1-(float(compteur_C0)/len(data))**2-(float(compteur_C1)/len(data))**2,0)
        else:
            dico[niveau]=("leaf"," ",1-(float(compteur_C0)/len(data))**2-(float(compteur_C1)/len(data))**2,1)
    if possible==True:                                  #if the stop conditions are not verified,then we do another iteration    
        maxGain=Gain2(data,split_possibles[0][0])[0]
        split_retenu=split_possibles[0]
        for i in split_possibles:       #we calculate the max of the Information Gain for the remaining split_possities
            a=Gain2(data,i[0])[0]
            if a>maxGain:
                maxGain=a
                split_retenu=i
        n_split_possibles=[]
        for i in split_possibles:
            if i[0][0]!=split_retenu[0][0]:        #we delete the split_possibility that we just used for the future and the other that corresponds to the same attribute
                n_split_possibles.append(i)
        if compteur_C0>compteur_C1:
            dico[niveau]=(split_retenu[0],Gain2(data,split_retenu[0])[0],GINI(data,split_retenu[0]),0)  #we put in the dico : the split that we choose the Information Gain, the GINI, and the max between C=0 and C=1 
        else:
            dico[niveau]=(split_retenu[0],Gain2(data,split_retenu[0])[0],GINI(data,split_retenu[0]),1)
        data1=Gain2(data,split_retenu[0])[1]                                 #we repeat again our function for the two sons
        data2=Gain2(data,split_retenu[0])[2]
        Iteration(data1,n_split_possibles,2*niveau,minNum,dico)
        Iteration(data2,n_split_possibles,2*niveau+1,minNum,dico)
       
            
            
            
            
            
split=[["A 0"],["A 0 1"],["A 0 1 2"],["B 0"],["B 0 1"]]


def GINI(data,attribute_split):
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
        N_C1_l0=len(l0)-N_C0_l0
        N_C1_l1=len(l1)-N_C0_l1
    s=(float(len(l0))/len(data))*(1-(float(N_C0_l0)/len(l0))**2-(float(N_C1_l0)/len(l0))**2)
    s2=(float(len(l1))/len(data))*(1-(float(N_C0_l1)/len(l1))**2-(float(N_C1_l1)/len(l1))**2)
    return s+s2




def BuldingDecisionTree(data,minNum=1):  #print the tree thanks to the global variable dico
    dico={}
    Iteration(data,split,1,minNum,dico)     #create the dictionnary dico, that we are going to print with te form recommended 
    for i in range(1,10):              #there are less than 10 nodes
        if i==1:
            print("\nRoot\nLevel 1\n"+"Feature "+dico[1][0]+"\n"+"Information Gain "+str(dico[1][1])+"\nGINI "+str(dico[1][2])+"\n")
        else :
            if 2*i in list(dico.keys()) or 2*i+1 in list(dico.keys()):       #then it is not a leaf, it is an Intermediate
                    print("Intermediate\nLevel "+str(int(math.log(i,2))+1)+"\nFeature "+str(dico[i][0])+"\nInformation Gain "+str(dico[i][1])+"\nGINI "+str(dico[i][2])+"\n")
            else:
                if i in list(dico.keys()):
                    print("Leaf\nLevel "+str(int(math.log(i,2))+1)+"\nGINI "+str(dico[i][2])+"\n")
    return dico
                    

def openfile(f):
    f=open(f,'r')
    res=[]
    for line in f:
        a,b,c= [int(x) for x in line.split()]
        res.append([a,b,c])
    return res
        

