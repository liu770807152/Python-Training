#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:58:22 2021

@author: angelinamou
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

# Question 1:  
def read_dataset(file):
    """
    Read CSV file 
    
    Parameter: Please input a file name
    """
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        table = [ row for row in reader ]
        for listi in range(len(table)):
            for datai in range(len(table[0])):
                table[listi][datai] = float(table[listi][datai])
    return table

def read_dataset1(file):
    list_total = []
    for j in range(883):
        for i in range(1189):
            number = file[j]
            number = number[i]
            list_total.append(number)
    return list_total

data_1list = read_dataset("elevation_data_small.csv")



step = 1
X = np.arange(0,1189,step)
Y = np.arange(-883,0,step)
#show the grid of x and y
XY_grid = np.meshgrid(X,Y)


"""data_1list = np.mat(data_1list)              
data_1list = np.array(data_1list)
data_1list.shape = (883,1189)"""

plt.figure(figsize=(10,6))
hset = plt.contourf(X,Y,data_1list)
hset = plt.contour(X,Y,data_1list)

#cset = plt.contourf(X,Y,data_1list,cmap=plt.cm.hot)

#画出8条线，并将颜色设置为黑色
contour = plt.contour(X,Y,data_1list,12,colors='k')
#等高线上标明z（即高度）的值，字体大小是10，颜色分别是黑色和红色
plt.clabel(contour,fontsize=10,colors='k')
#设置颜色条，（显示在图片右边）
plt.colorbar(hset)
plt.show()

# 545.64,545.65
contour = plt.contour(X,Y,data_1list,[550, 551],colors='k')
#等高线上标明z（即高度）的值，字体大小是10，颜色分别是黑色和红色
plt.clabel(contour,fontsize=10,colors='k')
plt.show()
