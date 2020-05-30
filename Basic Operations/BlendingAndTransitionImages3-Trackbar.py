import cv2

def emptyFunc():
    pass

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    
    imgpath1 = path + "4.2.01.tiff"
    imgpath2 = path + "4.2.03.tiff"
    
    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    
    windowName = "Image Blending"
    cv2.namedWindow(windowName)
    cv2.createTrackbar('Img1->Img2', windowName, 0, 50, emptyFunc)
    
    alpha = 1
    beta = 0
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)

    while(1):
        cv2.imshow(windowName, output)
        
        if cv2.waitKey(1) == 27:
            break
        
        alpha = (cv2.getTrackbarPos('Img1->Img2', windowName)/50)
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
       
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()