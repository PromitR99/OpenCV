import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath = "D:\\CODES\\OpenCV3\\DataSets\\4.2.07.tiff"
    img = cv2.imread(imgpath, 1)
    imgGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgFUN = cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img1 = cv2.imread(imgpath, 0)
    img2 = cv2.cvtColor(img1, cv2.COLOR_GRAY2RGB)
    img3 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    
    plt.imshow(img)
    plt.title('Image 1')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    
    plt.imshow(imgGRAY)
    plt.title('Image 1 - GRAY')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(imgFUN)
    plt.title('Image 1 - FUN')
    plt.xticks([])
    plt.yticks([])
    plt.show()
 
    
    plt.imshow(imgRGB)
    plt.title('Image 1 - RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img1)
    plt.title('Image 0')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img2)
    plt.title('Image 0 - Converted')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img3)
    plt.title('Image 0 - Converted2')
    plt.xticks([])
    plt.yticks([])
    plt.show()
 
 
if __name__ == "__main__":
    main()