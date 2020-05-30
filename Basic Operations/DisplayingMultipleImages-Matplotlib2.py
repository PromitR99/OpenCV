import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    
    imgpath1 = path + "4.2.01.tiff"
    imgpath2 = path + "4.2.03.tiff"
    imgpath3 = path + "4.2.05.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    img3 = cv2.imread(imgpath3, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
    
    titles = ['Liquid Drop','Baboon','Airplane']
    images = [img1, img2, img3]
    
    '''
    plt.subplot(<row_size>, <column_size>, <position>)
    =>We are defining a 2D grid
    =>2D array of <row_size>X<column_size>
    =><position> is the array-index of the image in the 2D array
    '''
    
    for i in range(4) :
            plt.subplot(2, 2, i+1) 
            plt.imshow(images[i])
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])
    
    plt.show() #Show as a grid

if __name__ == "__main__":
    main()

