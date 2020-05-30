import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    imgpath =  path + "4.2.07.tiff"

    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    Z = img.reshape((-1,3)) #going to prepare the image for K-means clustering
    Z = np.float32(Z) #type-casting unint8 to float32
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    #criteria for finding out the K-means clustering
    
    K=2 #clustering only with 2 clubs
    ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output1 = res1.reshape((img.shape))
    
    K=4
    ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS) #10 iterations
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()] #flattening
    output2 = res1.reshape((img.shape))
    
    K=12
    ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output3 = res1.reshape((img.shape))

    output = [img, output1, output2, output3]
    titles = ['Original Image', 'K=2', 'K=4', 'K=12']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()