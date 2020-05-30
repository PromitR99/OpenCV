import cv2

def main():
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    '''
    Webcam has default properties with numbers
    '''
    print('Width : ' + str(cap.get(3)))      #'3' prints height
    print('Height : ' + str(cap.get(4)))     #'4' prints width
    
    cap.set(3, 400)        #Sets '3'(Height) manually
    cap.set(4, 300)         #Sets '4'(Width) manually
    
    print('Width : ' + str(cap.get(3)))
    print('Height : ' +str(cap.get(4)))
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = cap.read()
        
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("Gray", output)
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27: #Waits for 'Esc' key
            break

    cv2.destroyAllWindows()    

    cap.release()

if __name__ == "__main__":
    main()