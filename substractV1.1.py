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

def showoneround(picdir,b,column=4,row=2):
    files = os.listdir(picdir)
    f1list = [s for s in files if s[-6:] == '1.tiff']
    f2list = [s for s in files if s[-6:] == '2.tiff']
    f1listsorted=sorted(f1list,key=(lambda x:int(x[-10:-7])))
    f2listsorted = sorted(f2list, key=(lambda x: int(x[-10:-7])))
    couplesfile= zip(f1listsorted,f2listsorted)[:8]
    # for pic in f1list:
    #     f1 += plt.imread(picdir + pic)
    # f1bin = bining(f1, b)
    # f2 = np.zeros((512, 512))
    # for pic in f2list:
    #     f2 += plt.imread(picdir + pic)
    # f2bin = bining(f2, b)
    #plt.subplot(122)
    # fabsbin = (f1bin - f2bin)/picnum/(b[0]*b[1])
    #fabsbin = (f2bin - f3bin) / (f1bin - f3bin)
    for i,couple in enumerate(couplesfile):
        f1bin=bining(plt.imread(picdir+couple[0]),b)
        f2bin=bining(plt.imread(picdir+couple[1]),b)
        fbin=(f1bin - f2bin)/(b[0]*b[1])
        tocounts=np.sum(fbin)
        if i%(column*row)==0:
            fig=plt.figure(figsize=(20, 20))
        print i
        ax2=fig.add_subplot(row,column,i%(column*row)+1)
        im2=ax2.imshow(np.rot90(fbin.transpose(),2), cmap='jet',vmin=100,vmax=200)
        ax2.set_title(couple[0][-10:-7]+' counts:%.2e'%tocounts)
        plt.colorbar(im2,ax=ax2)
    plt.show()

def showoneround2(picdir,b,ax2):
    files = os.listdir(picdir)
    f1list = [s for s in files if s[-6:] == '1.tiff']
    f2list = [s for s in files if s[-6:] == '2.tiff']
    f1 = np.zeros((512, 512))
    picnum=len(f1list)
    for pic in f1list:
        f1 += plt.imread(picdir + pic)
    f1bin = bining(f1, b)
    f2 = np.zeros((512, 512))
    for pic in f2list:
        f2 += plt.imread(picdir + pic)
    f2bin = bining(f2, b)
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
#    fig=plt.figure(figsize=(20, 20))
#    ax1=fig.add_subplot(1,2,1)
#    ax2=fig.add_subplot(1,2,2)
    print time.asctime()
    picdir = 'E:\\20170629\\0629Night\\etalonGallery01\\'
    showoneround(picdir,b)
    b = [4,4]
#    fig=plt.figure(figsize=(20, 20))
#    ax1=fig.add_subplot(1,2,1)
#    ax2=fig.add_subplot(1,2,2)
#    picdir = 'E:\\20170629\\0629Night\\Round03\\'
#    showoneround(picdir,b,ax1,ax2)
#    folder='E:\\20170629\\0629Night\\'
#    folderlist=[folder+x+'/' for x in os.listdir(folder) if x.startswith('Round') and os.path.isdir(folder+x)][:]
#    print folderlist
#    foldnum=len(folderlist)
#    columnum=4
#    rownum=foldnum/columnum+1
#    fig2=plt.figure(figsize=(20, 20))
#    for i in range(foldnum):
#        axy=fig2.add_subplot(rownum,columnum,i+1)
#        print i+1,
#        showoneround2(folderlist[i],b,axy)
