# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 22:40:04 2017

@author: OLB
"""

import matplotlib.pyplot as plt
import os
import numpy as np
import time


def bining(f, b):
    fshape = np.shape(f)
    binnedf1 = np.zeros((f.shape[0] / b[0], fshape[1]))
    for i in range(fshape[0] / b[0]):
        for j in range(b[0]):
            binnedf1[i, :] += f[i * b[0] + j, :]
    binnedf2 = np.zeros((f.shape[0] / b[0], fshape[1] / b[1]))
    for i in range(fshape[1] / b[1]):
        for j in range(b[1]):
            binnedf2[:, i] += binnedf1[:, i * b[1] + j]
    return binnedf2

def showoneround(picdir,b,ax1,ax2,origin=True):
    files = os.listdir(picdir)
    f1list = [s for s in files if s[-6:] == '1.tiff']
    f2list = [s for s in files if s[-6:] == '2.tiff']
    f3list = [s for s in files if s[-6:] == '3.tiff']
    f1 = np.zeros((512, 512))
    picnum=len(f1list)
    for pic in f1list:
        f1 += plt.imread(picdir + pic)
    f1bin = bining(f1, b)
    f2 = np.zeros((512, 512))
    for pic in f2list:
        f2 += plt.imread(picdir + pic)
    f2bin = bining(f2, b)
    f3 = np.zeros((512, 512))
    for pic in f3list:
        f3 += plt.imread(picdir + pic)
    f3bin = bining(f3, b)
    if origin==True:
        #ax1=fig.add_subplot(1,2,1)
        #plt.subplot(121)
        fabs = (f1 - f2) /picnum
        #fabs = (f2 - f3) / (f1 - f3) 
        im1=ax1.imshow(np.rot90(fabs.transpose(),2), cmap='jet',vmin=100,vmax=200)
        ax1.set_title(picdir[-8:-1])
        #ax1.colorbar()
        plt.colorbar(im1,ax=ax1)

    #plt.subplot(122)
    fabsbin = (f1bin - f2bin)/picnum/(b[0]*b[1])
    #fabsbin = (f2bin - f3bin) / (f1bin - f3bin)
    im2=ax2.imshow(np.rot90(fabsbin.transpose(),2), cmap='jet',vmin=100,vmax=200)
    ax2.set_title(picdir[-8:-1])
    plt.colorbar(im2,ax=ax2)
    
def showoneround2(picdir,b,ax2):
    files = os.listdir(picdir)
    f1list = [s for s in files if s[-6:] == '1.tiff']
    f2list = [s for s in files if s[-6:] == '2.tiff']
    f3list = [s for s in files if s[-6:] == '3.tiff']
    f1 = np.zeros((512, 512))
    picnum=len(f1list)
    for pic in f1list:
        f1 += plt.imread(picdir + pic)
    f1bin = bining(f1, b)
    f2 = np.zeros((512, 512))
    for pic in f2list:
        f2 += plt.imread(picdir + pic)
    f2bin = bining(f2, b)
    f3 = np.zeros((512, 512))
    for pic in f3list:
        f3 += plt.imread(picdir + pic)
    #f3bin = bining(f3, b)

    #plt.subplot(122)
    fabsbin = (f1bin - f2bin)/picnum/(b[0]*b[1])
    fabsbin=np.rot90(fabsbin.transpose(),2)
    print np.max(fabsbin)
#    maxindice=np.unravel_index(fabsbin.argmax(),fabsbin.shape)
#    ax2.axvline(x=maxindice[1],color='white')
#    ax2.axhline(y=maxindice[0],color='white')
    #fabsbin = (f2bin - f3bin) / (f1bin - f3bin)
    im2=ax2.imshow(fabsbin, cmap='jet',vmin=100,vmax=300)
    ax2.set_title('Binned '+picdir[-8:-1]+' ')
    plt.colorbar(im2,ax=ax2)
    

if __name__=='__main__':
    b = [4,4]
    fig=plt.figure(figsize=(20, 20))
    ax1=fig.add_subplot(1,2,1)
    ax2=fig.add_subplot(1,2,2)
    print time.asctime()
    picdir = 'E:\\20170626\\0626Morning\\Round01\\'
    showoneround(picdir,b,ax1,ax2)
    b = [4,4]
    fig=plt.figure(figsize=(20, 20))
    ax1=fig.add_subplot(1,2,1)
    ax2=fig.add_subplot(1,2,2)
    picdir = 'E:\\20170629\\0629Night\\Round03\\'
    showoneround(picdir,b,ax1,ax2)
    folder='E:\\20170629\\0629Night\\'
    folderlist=[folder+x+'\\' for x in os.listdir(folder) if x.startswith('Round') and os.path.isdir(folder+x)][:]
    print folderlist
    foldnum=len(folderlist)
    columnum=4
    rownum=foldnum/columnum+1
    fig2=plt.figure(figsize=(20, 20))
    for i in range(foldnum):
        axy=fig2.add_subplot(rownum,columnum,i+1)
        print i+1,
        showoneround2(folderlist[i],b,axy)
