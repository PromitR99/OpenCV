import cv2

def main():
    
    path = "D:\\CODES\\OpenCV3\\DataSets\\"
    imgpath =  path + "4.2.03.tiff"
    img = cv2.imread(imgpath, 1)

    
    output = cv2.resize( img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR )
   
    
    cv2.imshow('Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    main()