import cv2
#import matplotlib.pyplot as plt
import numpy as np

def main():
    
    imgpath="D:\\CODES\\OpenCV3\\Advanced\\4.1.04-damaged.tiff"
    img=cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    rows, columns = img.shape    
    output = np.zeros(img.shape, np.uint8)
    
    for i in range(rows):
        for j in range(columns):
            if img[i][j] < 5:
                output[i][j] = 255

    outpath="D:\\CODES\\OpenCV3\\Advanced\\4.1.04-mask.tiff"
    cv2.imwrite(outpath, output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()