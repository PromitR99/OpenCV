import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath = "D:\\CODES\\OpenCV3\\DataSets\\4.2.07.tiff"
    img = cv2.imread(imgpath, 0)
    img1 = cv2.imread(imgpath, 1)
    
    
    plt.imshow(img)
    plt.title('Default Colormap 0')
    plt.show()
    
    plt.imshow(img, cmap='gray')
    plt.title('Gray Colormap 0')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img, cmap='gist_ncar')
    plt.title('Fun 0')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img1)
    plt.title('Default Colormap 1')
    plt.show()
    
    plt.imshow(img1, cmap='gray')
    plt.title('Gray Colormap 1')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    plt.imshow(img1, cmap='gist_ncar')
    plt.title('Fun 1')
    plt.xticks([])
    plt.yticks([])
    plt.show()


if __name__ == "__main__":
    main()