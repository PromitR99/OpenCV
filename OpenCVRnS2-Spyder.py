# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:19:15 2019

@author: asus
"""

import cv2

def main():
    imgpath="D:\\CODES\\OpenCV3\\DataSets\\4.1.01.tiff"
    img1=cv2.imread(imgpath, 1)
    img2=cv2.imread(imgpath, 0)
    img3=cv2.imread(imgpath, -1)
    cv2.namedWindow('Pic1', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Pic0', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Pic-1', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Pic1', img1)
    cv2.imshow('Pic0', img2)
    cv2.imshow('Pic-1', img3)
    outpath="D:\\CODES\\OpenCV3\\OUTPUT\\4.1.01.1.jpg"
    cv2.imwrite(outpath, img1)
    outpath="D:\\CODES\\OpenCV3\\OUTPUT\\4.1.01.0.jpg"
    cv2.imwrite(outpath, img2)
    outpath="D:\\CODES\\OpenCV3\\OUTPUT\\4.1.01.-1.jpg"
    cv2.imwrite(outpath, img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()