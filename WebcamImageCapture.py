import cv2
import matplotlib.pyplot as plt

def main():
    cap = cv2.VideoCapture(0) #If multiple cameras are attached to Computer. You can chose any one of them through cv2.VideoCapture(n)
    
    '''
    If 5 WebCamsare attached to it.
    cap1 = cv2.VideoCapture(0)
    .
    .
    .
    cap5 = cv2.VideoCapture(4)
    '''
    
    if cap.isOpened(): # Checks if camera is opened
        ret, frame = cap.read()
        '''
        cap.read() captures image at that moment.
        Returns status to varialbe 'ret'. 'True' if it captures image, else 'False'.
        'frame' stores the matrix of the image.
        '''
        print(ret) # Returns 'True' if WebCam is working, else 'False'
        print(frame)
    else:
        ret = False
        
    '''
    Above code checks if Webcam is working
    '''

    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Coverts BGR to RGB
 
    
    plt.imshow(img1)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    

    cap.release() #Releases the associated Webcam(s) from operation

if __name__ == "__main__":
    main()