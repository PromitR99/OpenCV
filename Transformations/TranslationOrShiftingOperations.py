import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    imgpath1 =  path + "4.2.03.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    T = np.float32([[1, 0, 50], [0, 1, -150]])
    
#    print(T)
    
    
    output = cv2.warpAffine(img1, T, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Shifted Image')
    plt.show()

if __name__ == "__main__":
    main()