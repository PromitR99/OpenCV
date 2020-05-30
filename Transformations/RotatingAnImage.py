import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    imgpath1 =  path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    R = cv2.getRotationMatrix2D((columns/2, rows/2), 45, 0.75)
    
    print(R)
    
    output = cv2.warpAffine(img1, R, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Rotated Image')
    plt.show()

if __name__ == "__main__":
    main()