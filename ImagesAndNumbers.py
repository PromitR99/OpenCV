# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 09:00:57 2019

@author: asus
"""

import cv2

def main():
    imgpath="D:\\CODES\\OpenCV3\\DataSets\\4.2.01.tiff"
    img1=cv2.imread(imgpath, 1)
    print(img1) #prints the information of the image that is sent to the kernel 
    print(type(img1)) #prints data-type of the information 
    print(img1.dtype) #prints data-type of basic building block of the information
    print(img1.shape)
    print(img1.ndim)
    print(img1.size)
    print("\n")
    img2=cv2.imread(imgpath, 0)
    print(img2) #prints the information of the image that is sent to the kernel 
    print(type(img2)) #prints data-type of the information 
    print(img2.dtype) #prints data-type of basic building block of the information
    print(img2.shape)
    print(img2.ndim)
    print(img2.size)
    #cv2.namedWindow('Pic', cv2.WINDOW_AUTOSIZE)
    #cv2.imshow('Pic', img)
    #cv2.waitKey(0)
    #cv2.destroyWindow('Pic')
    
if __name__ == "__main__":
    main()