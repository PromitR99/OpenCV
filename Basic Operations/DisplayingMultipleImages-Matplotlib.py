import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    
    imgpath1 = path + "4.2.01.tiff"
    imgpath2 = path + "4.2.07.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    '''
    plt.subplot(<row_size>, <column_size>, <position>)
    =>We are defining a 2D grid
    =>2D array of <row_size>X<column_size>
    =><position> is the array-index of the image in the 2D array
    '''
    
    plt.subplot(1, 2, 1) 
    plt.imshow(img1)
    plt.title('Liquid Drop')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    plt.imshow(img2)
    plt.title('Vegetables')
    plt.xticks([])
    plt.yticks([])
    
    plt.show() #Show as a grid

if __name__ == "__main__":
    main()