#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:38:11 2019

@author: paul
"""

### Question 3 : Prunned Tree

import Question2


def Pruned_tree(dico,alpha,data):               #we calculate the gen_error without a part of the tree
                                                #if the gen_error is improved, we keep only this part of the tree
                                                #the maximum of node is seven, we use this but we could have done this function in a more general case
                                                
    initial_error=Question2.Generalization_error(data,dico,alpha)
    if 7 in list(dico.keys()):
        new_dico={}
        for i in range(1,6):
            if i in list(dico.keys()):
                if i==3:
                    new_dico[i]=("leaf","pas de gain",dico[3][2],dico[3][3])
                else:
                    new_dico[i]=dico[i]
        #print(new_dico)
        new_error=Question2.Generalization_error(data,new_dico,alpha)
        if new_error<initial_error:                                           #then it is better to supress nodes 6 and 7 
            print("suppression of nodes 6 and 7 and 3 becomes a leaf")    
            dico=new_dico        
        initial_error=new_error
    if 5 in list(dico.keys()):
        new_dico2={}
        for i in range(1,4):
            if i in list(dico.keys()):
                if i==2:
                    new_dico2[i]=("leaf","pas de gain",dico[2][2],dico[2][3])
                else:
                    new_dico2[i]=dico[i]
        for i in range(6,8):
            if i in list(dico.keys()):
                new_dico2[i]=dico[i]    
        new_error=Question2.Generalization_error(data,new_dico2,alpha)     #then it is better to supress nodes 4 and 5 
        if new_error<initial_error:
            dico=new_dico2
            print("suppression of nodes 4 and 5 and 2 becomes a leaf") 
    return dico
            
    


