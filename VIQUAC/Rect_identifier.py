import cv2
def specific_area(filename):
    img = cv2.imread(filename) 

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    thresh = cv2.threshold(blurred, 125, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh,None,iterations = 1)
    src_color =(0)
    src_color1=(100)
    src_color2=(100)
    src_color3=(255)
    mask = cv2.inRange(thresh, src_color, src_color1)
    mask1 = cv2.inRange(thresh, src_color2, src_color3)
    thresh[mask > 0] = [0]
    thresh[mask1 > 0] = [0]
    bw=thresh.copy()
    bw[mask>0] = (255)
    cv2.imshow('Specific Area',bw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    contours,hierarchy = cv2.findContours(bw,cv2.RETR_TREE,
                                          cv2.CHAIN_APPROX_SIMPLE)
    area=[]
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cc=w*h
        area.append(cc)
        bw=cv2.rectangle(bw,(x,y),(x+w,y+h),(0,255,0),2)
        
    c=(area.index(max(area)))
    x,y,w,h = cv2.boundingRect(contours[c])
    #bw=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cc=img[y:y+h,x:x+w]
    cv2.imshow('Specific Area',cc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return cc
# specific_area("Example_1.jpeg")