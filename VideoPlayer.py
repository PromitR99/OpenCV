import cv2

def emptyFunc():
    pass

def main():
    windowName = "OpenCV Video Player"
    cv2.namedWindow(windowName)
    cv2.createTrackbar('speed', windowName, 15, 60, emptyFunc)
    
    filename = 'D:\\CODES\\OpenCV3\\OUTPUT\\WebcamVidRec.avi'
    cap = cv2.VideoCapture(filename)

    while (cap.isOpened()):
        
        ret, frame = cap.read()
        
        #print(ret)
        
        if ret:   
            cv2.imshow(windowName, frame)
            
            speed=cv2.getTrackbarPos('speed', windowName)
            
            if cv2.waitKey(speed) == 27: 
                  break
            
        else :
            break

    cv2.destroyAllWindows()     
    cap.release()

if __name__ == "__main__":
    main()