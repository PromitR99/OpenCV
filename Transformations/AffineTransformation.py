import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    imgpath1 =  path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    point1 = np.float32([[0, 0], [500, 0], [250, 500]])
    point2 = np.float32([[100, 100], [450, 100], [200, 450]])
    
    A = cv2.getAffineTransform(point1, point2)
    
    print(A)
    
    
    output = cv2.warpAffine(img1, A, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Transformed Image')
    plt.show()

if __name__ == "__main__":
    main()