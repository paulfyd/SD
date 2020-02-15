#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:50:33 2019

@author: paul
"""


## Question 2 : Generalization error

## Please read the very short notice


def Elementary_Test(liste,dico,index):        #return the new index in the dico, according to the condition of the tree at the actual index
                                              #liste has the form liste=[a,b,c]
    if 2*index not in list(dico.keys()) and 2*index+1 not in list(dico.keys()):  #if we are on the index of a leaf
        return -1
    else:                                #else we look at the condition and see if it is respected by the liste 
        if dico[index][0]=="A 0":        #if it is respected, we go down at the left, thus at the index 2*index
            if liste[0]==0:
                return 2*index
            else : 
                return 2*index+1        #on the contrary, we go down to the right, at 2*index+1
        if dico[index][0]=="A 0 1":
            if liste[0]==0 or liste[0]==1:
                return 2*index
            else : 
                return 2*index+1
        if dico[index][0]=="A 0 1 2":
            if liste[0]==3:
                return 2*index+1
            else : 
                return 2*index
        if dico[index][0]=="B 0":
            if liste[1]==0:
                return 2*index
            else : 
                return 2*index+1
        if dico[index][0]=="B 0 1":
            if liste[1]==0 or liste[1]==1 :
                return 2*index
            else : 
                return 2*index+1

       
def Test(liste,dico):                           #we repeat the elementary tests until we are at a leaf, ie we go down the tree
    a=1
    while Elementary_Test(liste,dico,a)!=-1:
        a=Elementary_Test(liste,dico,a)
    if liste[2]==dico[a][3]:
        return True
    return False

def Generalization_error(data,dico,alpha):       #we do the test for every piece of data, to calculate the number of error
    number_errors=0                                    #we count the number of leaves
    number_leaves=0                                    #we return erreurs+alpha*number_of_leaves
    for i in data:
        if Test(i,dico)==False:
            number_errors+=1
    for i in list(dico.keys()):
        if dico[i][0]=="leaf":
           number_leaves+=1
    print("The generalization error is "+str(number_errors+alpha*number_leaves))
    return number_errors+alpha*number_leaves
    