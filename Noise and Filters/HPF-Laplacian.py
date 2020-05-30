import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    imgpath =  path + "5.1.11.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edges = cv2.Laplacian(img, -1, ksize=5, scale=1, delta=0, 
                          borderType=cv2.BORDER_DEFAULT)
    #ksize(kernel size) have to be an odd number and not larger than 31

    output = [img, edges]
    titles = ['Original', 'Edges']
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(output[i], cmap = 'gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()