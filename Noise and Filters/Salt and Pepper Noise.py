import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    imgpath =  path + "4.1.03.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    rows, columns, channels = img.shape
    p = 0.05
    
    output = np.zeros(img.shape, np.uint8)
    #creates an array of the order of 'img'-matrix with all elements as 0.

#    output = np.ones((3,3), np.uint32) =>creates an array of order 3 with all elements as 1.
    
    for i in range(rows):
        for j in range(columns):
            r = random.random()
            if r < p/2:
                # pepper sprinkled
                output[i][j] = [0, 0, 0]
            elif r < p:
                # salt sprinkled
                output[i][j] = [255, 255, 255]
            else:
                output[i][j] = img[i][j]
  
    plt.imshow(output)
    plt.title('Image with Salt and Pepper Noise')
    plt.show()

if __name__ == "__main__":
    main()