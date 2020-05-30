import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    imgpath =  path + "4.2.07.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    k = np.array(([0, 0, 0], 
                  [0, 1, 0], 
                  [0, 0, 0]), np.float32)
    #creates an array: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    #Identity
    
#    k = np.array(([1, 0, -1], 
#                  [0, 0, 0], 
#                  [-1, 0, 1]), np.float32)
    #Edge Detection 1
    
#    k = np.array(([0, 1, 0], 
#                  [1, -4, 1], 
#                  [0, 1, 0]), np.float32)
    #Edge Detection 2
    
#    k = np.array(([-1, -1, -1], 
#                  [-1, 8, -1], 
#                  [-1, -1, -1]), np.float32)
    #Edge Detection 3
    
    
#    k = np.array(([0, -1, 0], 
#                  [-1, 5, -1], 
#                  [0, -1, 0]), np.float32)
    #Sharpen
    
#    k = np.array(np.ones((5, 5), np.float32))/27 
    #creates an array of order 3 with all element as 1/9. Order and values can be changed
    #Box Blur
    
#    k = np.array(([1, 2, 1], 
#                  [2, 4, 2], 
#                  [1, 2, 1]), np.float32)/16
    #Gaussian Blur
    
#    k = np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), np.float32)
    #creates an array: [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    
#    print(k)
    
#    print(type(k))
    

    output = cv2.filter2D(img, -1, k)
    
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    
    plt.subplot(1, 2, 2)
    plt.imshow(output)
    plt.title('Filtered Image')
    
    plt.show()

if __name__ == "__main__":
    main()