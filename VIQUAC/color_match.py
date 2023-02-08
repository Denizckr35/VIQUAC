import ral_to_list 
import image_reader
import cv2 as cv
from Rect_identifier import specific_area
def img_color_match(filename):
    try:
        difference=[]
        ral_numb,Dict=ral_to_list.ral_dict("ral_standard.csv")
        file=specific_area(filename)
        average_color,img=image_reader.average_color(file)
        for i in range(len(Dict)):
            dict_r1=Dict[ral_numb[i]][1][0]
            dict_g1=Dict[ral_numb[i]][1][1]
            dict_b1=Dict[ral_numb[i]][1][2]
            img_r1=average_color[0]
            img_g1=average_color[1]
            img_b1=average_color[2]
            cR=dict_r1-img_r1 
            cG=dict_g1-img_g1 
            cB=dict_b1-img_b1 
            uR=dict_r1+img_r1 
            distance=100-(cR*cR*(2+uR/256) + cG*cG*4 + cB*cB*(2+(255-uR)/256))**(1/3)
            difference.append(distance)
        a=difference.index(max(difference))
        x,y,z=img.shape
        r=Dict[ral_numb[a]][1][0]   
        g=Dict[ral_numb[a]][1][1]
        b=Dict[ral_numb[a]][1][2]
        img=cv.cvtColor(img,cv.COLOR_RGB2BGR)
        
        if x>y:
           img=cv.rotate(img,cv.ROTATE_90_CLOCKWISE )
           # x,y,z=img.shape
           
           img=cv.copyMakeBorder(img,0,0,0,x,cv.BORDER_CONSTANT,value=(b,g,r))
           img=cv.copyMakeBorder(img,0,80,0,0,cv.BORDER_CONSTANT,value=(255,255,255))     
           org = (0,y+30)
           org1= (0,y+65)
           print(x,y)
        elif y>x:
            img=cv.copyMakeBorder(img,0,0,0,y,cv.BORDER_CONSTANT,value=(b,g,r))
            img=cv.copyMakeBorder(img,0,80,0,0,cv.BORDER_CONSTANT,value=(255,255,255))
            org = (0,x+30) 
            org1= (0,x+65)
            
        max_dif=max(difference)
        matched_col=Dict[ral_numb[a]][0]
        font = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        color = (0,0,0)
        thickness = 2
        img=cv.putText(img,"Accuracy:{:.3f}%"
                       .format(max_dif),org,font,
                       fontScale,color,thickness,cv.LINE_AA)
        img=cv.putText(img,"Matched Color:{}"
                       .format(matched_col),org1,font,
                       fontScale,color,thickness,cv.LINE_AA)
        cv.imwrite("Output.png",img)
        # print(max(difference))
        # print(Dict[ral_numb[a]])
        return img
    except Exception as e:
        print(e)

# img_color_match("Example_1.jpeg")