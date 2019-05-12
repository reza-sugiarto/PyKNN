#!/usr/bin/env python
# coding: utf-8


import numpy as np
from math import sqrt,pow
import operator
from collections import Counter


class old_pyknn():
    '''
    This is KNN algorithm implemented in python
    
    This algorithm using euclidean distance to calculate distance.
    You can change on Distance Calculation Section. 
    
    
    ps: I know this a little slow. Help me to make it faster.
    '''
    __version__ = '0.2'
    __author__ ='Reza'

    def __init__(self):
        pass

    #Distance Calculation
    def euclid_dist(self,data_ts,data_tr):
        self.data_ts=data_ts
        self.data_tr=data_tr
        dist=0
        for i in range(len(data_tr)):
            dist+=pow((data_ts[i]-data_tr[i]),2)
        return sqrt(dist)
    
    #Checking Neighbor
    def neighbors_class(self,data_train,data_test,label_train,n):
        self.data_train=data_train
        self.data_test=data_test
        self.label_train=label_train
        self.n=n
        check_dist={}
        for i in range(data_train.shape[0]):
            dist=self.euclid_dist(data_train.iloc[i],data_test)
            ground_label=label_train.iloc[i][0] #check your y_train shape and choose manually which suitable. Cheers!
            #ground_label=label_train.iloc[i]
            check_dist.update({dist:ground_label})
        check_dist=sorted(check_dist.items(),key=operator.itemgetter(0))
        check_class=[]
        for i in range(n):
            temp_class=check_dist[i][1]
            check_class.append(temp_class)
        c=Counter(check_class)
        return c.most_common(1)[0][0]
    
class pyknn():
    '''
    This is KNN algorithm implemented in python
    
    This algorithm using euclidean distance to calculate distance.
    You can change on Distance Calculation Section. 
    
    
    ps: I know this a little slow. Help me to make it faster.
    '''
    __version__ = '1'
    __author__ ='Reza'

    def __init__(self,train_data,train_label,n):
        self.train_data=train_data
        self.train_label=train_label
        self.n=n
        
    #Distance Calculation
    def euclid_dist(self,data_ts,data_tr):
        self.data_ts=data_ts
        self.data_tr=data_tr
        dist=0
        for i in range(len(data_tr)):
            dist+=pow((data_ts[i]-data_tr[i]),2)
        return sqrt(dist)
    
    #Checking Neighbor
    def neighbors_class(self,data_test):
        self.data_test=data_test
        check_dist={}
        for i in range(self.train_data.shape[0]):
            dist=self.euclid_dist(self.train_data.iloc[i],data_test)
            ground_label=self.train_label.iloc[i][0] #check your y_train shape and choose manually which suitable. Cheers!
            #ground_label=label_train.iloc[i]
            check_dist.update({dist:ground_label})
        check_dist=sorted(check_dist.items(),key=operator.itemgetter(0))
        check_class=[]
        for i in range(self.n):
            temp_class=check_dist[i][1]
            check_class.append(temp_class)
        c=Counter(check_class)
        return c.most_common(1)[0][0]
    
    
    