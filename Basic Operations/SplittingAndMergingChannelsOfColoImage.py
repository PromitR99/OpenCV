import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    
    imgpath1 =  path + "4.2.03.tiff"
    
    img = cv2.imread(imgpath1, 1)
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    r, g, b = cv2.split(img1)
    h, s, v = cv2.split(img2)
    
    titles = ['OriginalImage1', 'Red', 'Green', 'Blue', 'OriginalImage2(HSV)', 'Hue', 'Saturation', 'Value']
    images = [cv2.merge((r, g, b)), r, g, b, cv2.merge((h, s, v)), h, s, v]

    
    plt.subplot(2, 4, 1)
    plt.imshow(images[0])
    plt.title(titles[0])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 4, 2)
    plt.imshow(images[1], cmap='Reds')
    plt.title(titles[1])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 4, 3)
    plt.imshow(images[2], cmap='Greens')
    plt.title(titles[2])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 4, 4)
    plt.imshow(images[3], cmap='Blues')
    plt.title(titles[3])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 4, 5)
    plt.imshow(images[4])
    plt.title(titles[4])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 4, 6)
    plt.imshow(images[5], cmap='Greys')
    plt.title(titles[5])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 4, 7)
    plt.imshow(images[6], cmap='Greys')
    plt.title(titles[6])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 4, 8)
    plt.imshow(images[7], cmap='Greys')
    plt.title(titles[7])
    plt.xticks([])
    plt.yticks([])

    plt.show()  
 
if __name__ == "__main__":
    main()