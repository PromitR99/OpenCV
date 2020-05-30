import cv2

def main():
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    '''
    We need to create a 'VideoWriter' object.
    '''
    
    filename = 'D:\\CODES\\OpenCV3\\OUTPUT\\WebcamVidRec.avi'
    codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    framerate = 30
    resolution = (640, 480)
    
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)  #Here, we need to pass the appropriate parameters. All arguments can be written in th form of parameters also.
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = cap.read()
        
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Using colorspace
        
        VideoFileOutput.write(frame)  #In this object, we need to pass the current frame as argument in order for the function to write on thee disc. 
        
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27: #Waits for 'Esc' key
            break

    cv2.destroyAllWindows()    
    VideoFileOutput.release()  #In this object, we need to close the file when we exit the program.
    cap.release()

if __name__ == "__main__":
    main()