import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    
    imgpath1 = path + "4.2.01.tiff"
    imgpath2 = path + "4.2.03.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    alpha = 0.5
    beta = 0.5
    gamma = 0
    
    output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    
    add = img1+img2
    
    titles = ['Img1','Img2','WeightedSum','Sum']
    images = [img1, img2, output, add]
    
    for i in range(4) :
            plt.subplot(2, 2, i+1) 
            plt.imshow(images[i])
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])
    
    plt.show() #Show as a grid

if __name__ == "__main__":
    main()

