# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:33:42 2019

@author: asus
"""

import cv2
import numpy as np

def main():
    
    img=np.zeros((512, 512, 3), np.uint8)
    cv2.line(img, (0,99), (99,0), (255,0,0), thickness=2)
    cv2.rectangle(img, (400, 450), (450, 500), (253, 134, 87), thickness=3)
    cv2.circle(img, (256, 256), 30, (56, 255, 0), thickness=2)
    cv2.ellipse(img, (400,200), (50,20), 0, 0, 270, (127, 127, 127), thickness=-1)
    
    points=np.array([[80,2],[333, 78],[126, 9],[500,0],[44,500]], dtype=np.int32, copy=True)
    points=points.reshape((-1,1,2))
    cv2.polylines(img, [points], True, (200,100,50), thickness=1)
    
    text = 'Test'
    cv2.putText(img, text, (50,400), cv2.FONT_HERSHEY_TRIPLEX, 5, (255, 255, 0), thickness=3)
    
    #https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html#cv2.rectangle
    
    cv2.imshow('ShapesAndTexts', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()