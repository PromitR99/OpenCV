# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:19:15 2019

@author: asus
"""

import cv2

def main():
    imgpath="D:\\CODES\\OpenCV3\\DataSets\\4.2.01.tiff"
    img=cv2.imread(imgpath)
    cv2.namedWindow('Pic', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Pic', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Pic')
    
if __name__ == "__main__":
    main()
