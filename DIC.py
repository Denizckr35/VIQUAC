import os
import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import math

def image_folder_handler():
  
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    valid_images = [".jpg",".gif",".png",".tga",".jpeg",".tif"]
    list_of_images=[]
    for f in os.listdir(folder_path):
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue
        list_of_images.append(os.path.join(folder_path,f))
        # img = cv2.imread(os.path.join(folder_path,f))
        # print(list_of_images)
        
    return list_of_images
        

def img_loader(list_of_images):
    len_of_list=len(list_of_images)
    if len_of_list > 1:
        for count in range(len_of_list):
            if count==(len_of_list-1):
                break
            img_1=cv2.imread(list_of_images[count])
            img_2=cv2.imread(list_of_images[count+1])
    b=cv2.imread(list_of_images[0])
    cv2.imshow("DIC",b)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
# vector_positins()
#%% Roi Drawer Function 
def roi_drawer(img,roi_switch):
    global ix,iy,fx,fy,roı_check,drawing
    try:
            
        if roi_switch==1:
            img=cv2.imread(img)
            img_temp=img.copy()
        if roi_switch==2:
    
            img_temp=img.copy()
            
        # Start drawing on left mouse button event
        drawing = False
        
        # Define starting and ending points for line
        ix, iy = -1, -1 
        fx, fy = -1, -1
        roı_check=False
    
       
        # Mouse callback function
        def draw_shape(event, x, y, flags, param):
            global fx,fy,ix, iy,drawing,roı_check
        
            if event == cv2.EVENT_LBUTTONDOWN:
                drawing = True
                ix, iy = x, y
                
            elif event == cv2.EVENT_MOUSEMOVE:
                
                if drawing == True:
                    
                    img[:] =img_temp
                    
                    x = max(0, min(x, img.shape[1]))
                    y = max(0, min(y, img.shape[0]))
                    ix = max(0, min(ix, img.shape[1]))
                    iy = max(0, min(iy, img.shape[0]))
                    
                    cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
                     
            elif event == cv2.EVENT_LBUTTONUP:
                drawing = False
                x = max(0, min(x, img.shape[1]))
                y = max(0, min(y, img.shape[0]))
                ix = max(0, min(ix, img.shape[1]))
                iy = max(0, min(iy, img.shape[0]))
                
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
                fx,fy=x,y 
                roı_check=True
         
        # Bind the function to window
        if roi_switch==1:    
            cv2.namedWindow('Select Region Of Interest')
            cv2.setMouseCallback('Select Region Of Interest', draw_shape)
        
            reset=False
            
            while(1):
                
                cv2.imshow('Select Region Of Interest', img)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('x'):
                    reset = True
                elif key == 27:
                    break
            
                if reset:
                    img[:] = img_temp
                    reset = False
                    roı_check=False
            cv2.destroyAllWindows()
            img[:] = img_temp
            dikdörtgen_noktaları_First_Roi=[]
            if ix<0 or iy<0 or fx<0 or fy<0:
                print(ix,iy,fx,fy,"Hatalı Seçim.")
                pass
            else:
                dikdörtgen_noktaları_First_Roi.append([ix,iy,fx,fy])   
                return ix,iy,fx,fy,dikdörtgen_noktaları_First_Roi,roı_check
        
        
        elif roi_switch==2:
            cv2.namedWindow('Select Subset Region Of Interest')
            cv2.setMouseCallback('Select Subset Region Of Interest', draw_shape)
        
            reset=False
            
            while(1):
                
                cv2.imshow('Select Subset Region Of Interest', img)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('x'):
                    reset = True
                elif key == 27:
                    break
            
                if reset:
                    img[:] = img_temp
                    reset = False
                    roı_check=False
            cv2.destroyAllWindows()
            img[:] = img_temp
            dikdörtgen_noktaları_Subset_Roi=[]
             
            
            if ix<0 or iy<0 or fx<0 or fy<0:
                print(ix,iy,fx,fy,"Hatalı Seçim .")
                pass
            else:
                dikdörtgen_noktaları_Subset_Roi.append([ix,iy,fx,fy])    
                return ix,iy,fx,fy,dikdörtgen_noktaları_Subset_Roi,roı_check
    
    except Exception as e:
        print(e)
        pass
        
    
img = "C:/Users/deniz/Desktop/ohtcfrp_01.tif"

dikdörtgen_noktaları_First_Roi=roi_drawer(img,1) 

# print(1)
#%% First ROI Function


def first_ROI(img,dikdörtgen_noktaları_First_Roi):
    try:
        
        img=cv2.imread(img)
        ix,iy,fx,fy,_,roı_check=dikdörtgen_noktaları_First_Roi 
        roı_check_eşitlik=False
    
        
        if roı_check==True:
            if ix>fx and iy<fy:#Sol alt
                iix,ifx=fx,ix
                ix=iix
                fx=ifx
                roi_img=img[iy:fy,ix:fx]
            elif ix>fx and iy>fy:
                iix,ifx=fx,ix
                iiy,ify=fy,iy
                ix=iix
                fx=ifx
                iy=iiy
                fy=ify
                roi_img=img[iy:fy,ix:fx]
            elif ix<fx and iy>fy:
                iiy,ify=fy,iy
                iy=iiy
                fy=ify
                roi_img=img[iy:fy,ix:fx]
            elif ix==fx and iy==fy:
                roı_check_eşitlik=True
            else:
                roi_img=img[iy:fy,ix:fx]
            
            if roı_check_eşitlik==False:
                pass
            elif roı_check_eşitlik==True:
                print("Alan Seçilmedi.")
        return roi_img
    except Exception as e:
        print(e)
        pass    
        
        
roi_img_1=first_ROI(img,dikdörtgen_noktaları_First_Roi)
#%%
# print(2)
#%% Subset ROI Function

def subset_ROI(img,dikdörtgen_noktaları_Subset_Roi,dikdörtgen_noktaları_First_Roi):
    
    # img=cv2.imread(img)
    try:
        ix,iy,fx,fy,_,_=dikdörtgen_noktaları_First_Roi
        six,siy,sfx,sfy,_,roı_check=dikdörtgen_noktaları_Subset_Roi 
        
    
        
        
        roı_check_eşitlik=False
        
    
        if roı_check==True:
            if six>sfx and siy<sfy:
                iix,ifx=sfx,six
                six=iix
                sfx=ifx
                roi_img=img[siy:sfy,six:sfx]
            elif six>sfx and siy>sfy:
                iix,ifx=sfx,six
                iiy,ify=sfy,siy
                six=iix
                sfx=ifx
                siy=iiy
                sfy=ify
                roi_img=img[siy:sfy,six:sfx]
            elif six<sfx and siy>sfy:
                iiy,ify=sfy,siy
                siy=iiy
                sfy=ify
                roi_img=img[siy:sfy,six:sfx]
            elif six==sfx and siy==sfy:
                roı_check_eşitlik=True
            else:
                roi_img=img[siy:sfy,six:sfx]
            
            if roı_check_eşitlik==False:
                pass
            elif roı_check_eşitlik==True:
              print("Alan Seçilmedi.")  
        return roi_img
    except Exception as e:
        print(e)
        pass
#%%
# print(3)
#%%
dikdörtgen_noktaları_Subset_Roi=roi_drawer(roi_img_1,2) 
#%%
# print(4)
#%%
subset_roi_img=subset_ROI(roi_img_1,dikdörtgen_noktaları_Subset_Roi,dikdörtgen_noktaları_First_Roi)
#%%
# print(5)
#%%
def points_for_sub_roi_on_template(dikdörtgen_noktaları_First_Roi,dikdörtgen_noktaları_Subset_Roi):
    try:
        ix,iy,fx,fy,_,_=dikdörtgen_noktaları_First_Roi
        six,siy,sfx,sfy,_,_=dikdörtgen_noktaları_Subset_Roi 
        first_roi=[]
        second_roi=[]
    
            
        if ix>fx and iy<fy:#Sol alt
            iix,ifx=fx,ix
            ix=iix
            fx=ifx
            first_roi=[ix,iy,fx,fy]
        elif ix>fx and iy>fy:
            iix,ifx=fx,ix
            iiy,ify=fy,iy
            ix=iix
            fx=ifx
            iy=iiy
            fy=ify
            first_roi=[ix,iy,fx,fy]
        elif ix<fx and iy>fy:
            iiy,ify=fy,iy
            iy=iiy
            fy=ify
            first_roi=[ix,iy,fx,fy]
    
        elif ix<fx and iy<fy:
            first_roi=[ix,iy,fx,fy]
            
        if six>sfx and siy<sfy:
            iix,ifx=sfx,six
            six=iix
            sfx=ifx
            second_roi=[six,siy,sfx,sfy]
        elif six>sfx and siy>sfy:
            iix,ifx=sfx,six
            iiy,ify=sfy,siy
            six=iix
            sfx=ifx
            siy=iiy
            sfy=ify
            second_roi=[six,siy,sfx,sfy]
        elif six<sfx and siy>sfy:
            iiy,ify=sfy,siy
            siy=iiy
            sfy=ify
            second_roi=[six,siy,sfx,sfy]
        elif six<sfx and siy<sfy:
            second_roi=[six,siy,sfx,sfy]
            
        ix,iy,fx,fy=first_roi[0],first_roi[1],first_roi[2],first_roi[3]
        six,siy,sfx,sfy=second_roi[0],second_roi[1],second_roi[2],second_roi[3]
        
        tix=ix+six
        tiy=iy+siy
        tfx=ix+sfx
        tfy=iy+sfy
        main_roi_of_subset=[tix,tiy,tfx,tfy]
        return main_roi_of_subset,first_roi,second_roi
    except Exception as e:
        print(e)
        pass
# print(6)
pre_vector_list=points_for_sub_roi_on_template(dikdörtgen_noktaları_First_Roi,dikdörtgen_noktaları_Subset_Roi)
# print(7)
#%% Vector

def vector_positions(img,pre_vector_list):
    global eraser_dec,kayıt_kac_kere_oldu,rec_count,kayıt_dict
    try:    
    # Create a black image
        image = cv2.imread(img)
        
        
        main_roi_of_subset,first_roi,second_roi=pre_vector_list
        
        tix,tiy,tfx,tfy=main_roi_of_subset[0],main_roi_of_subset[1],main_roi_of_subset[2],main_roi_of_subset[3]
        ix,iy,fx,fy=first_roi[0],first_roi[1],first_roi[2],first_roi[3]
        six,siy,sfx,sfy=second_roi[0],second_roi[1],second_roi[2],second_roi[3]
        
        snix=ix+six
        sniy=iy+siy
        snfx=ix+sfx
        snfy=iy+sfy

        # Subset Step seçilir
        
        # subset_step=10
        scale_fact=10
        kayıt_kac_kere_oldu=0
        
        kayıt_dict={"rectangle":[],"circle":[],"free-form":[]}
        def subset_point_drawer(image,scale_fact,erase=False,mode=None,
                                kayıt=False,area=None,rect_area=None,
                                circle_area=None,form_area=None):
            global subset_vector_points_list,eraser_dec,kayıt_kac_kere_oldu,kayıt_dict
            
            height,width,_=image.shape 
            roi_black_and_white = np.zeros((height,width , 3), np.uint8)
            
            if erase==True:
                eraser_dec=True
                
                # print(rect_area)
                print("kac",kayıt_kac_kere_oldu)
                
                if kayıt==True:
                    
                    if kayıt_kac_kere_oldu==0:
                        
                        kayıt_kac_kere_oldu+=1 
                        
                    elif kayıt_kac_kere_oldu>0:
                        
                        
                        
                        
                        if mode=="rectangle":
                            
                            # kayıt_dic["rectangle"]=
                            
                            
                            ex,ey,efx,efy=area
                            erase_point_list=[]
                            subset_vector_points_list=[]
                            
                            for y in range(ey,efy):
                                for x in range(ex,efx):
                                    erase_point_list.append((x,y))
                                    
                            for y in range(height):
                                for x in range(width):
                                    if tix<x<tfx and tiy<y<tfy:
                                        roi_black_and_white[y,x]=255,255,255
                                        
                                        if y % scale_fact == 0 and x % scale_fact == 0 :
                                            subset_vector_points_list.append((x,y))
                                            # cv2.line(image,(x,y), (x, y), (0,0, 255), 4)
                                    
                                    elif ix<x<fx and iy<y<fy:
                                        roi_black_and_white[y,x]=255,255,255
                            
                            set1=set(subset_vector_points_list)   
                            set2=set(erase_point_list)        
                            
                            common=set1.intersection(set2)
                            result=[element for element in subset_vector_points_list if element not in common ]
                            
                            for ind,val in enumerate(result):
                                x,y=val
                                cv2.line(image,(x,y), (x, y), (0,0, 255), 4)
                            
                            
                            for y in range(ey,efy):
                                for x in range(ex,efx):
                                    roi_black_and_white[y,x]=0,0,0
                                    
                                    
                            # Count Section
                            
                            
                             
                            kayıt_dict["rectangle"].append({kayıt_kac_kere_oldu:1})
                            
                            kayıt_kac_kere_oldu+=1 
                        
                    elif mode=="circle": None 
                    elif mode=="free-form": None 
                   
                   
                   # elif mode=="rectangle": None 
                    
                    
                    
                elif kayıt==False:
  
                    if mode=="rectangle":
                        ex,ey,efx,efy=area
                        erase_point_list=[]
                        subset_vector_points_list=[]
                        
                        for y in range(ey,efy):
                            for x in range(ex,efx):
                                erase_point_list.append((x,y))
                                
                        for y in range(height):
                            for x in range(width):
                                if tix<x<tfx and tiy<y<tfy:
                                    roi_black_and_white[y,x]=255,255,255
                                    
                                    if y % scale_fact == 0 and x % scale_fact == 0 :
                                        subset_vector_points_list.append((x,y))
                                        # cv2.line(image,(x,y), (x, y), (0,0, 255), 4)
                                
                                elif ix<x<fx and iy<y<fy:
                                    roi_black_and_white[y,x]=255,255,255
                        set1=set(subset_vector_points_list)   
                        set2=set(erase_point_list)        
                        common=set1.intersection(set2)
                        result=[element for element in subset_vector_points_list if element not in common ]
                        
                        for ind,val in enumerate(result):
                            x,y=val
                            cv2.line(image,(x,y), (x, y), (0,0, 255), 4)
                        
                        
                        for y in range(ey,efy):
                            for x in range(ex,efx):
                                roi_black_and_white[y,x]=0,0,0
                        
                    elif mode=="circle":
                        ex,ey,efx,efy=area
                        erase_point_list=[]
                        subset_vector_points_list=[]
                   
                        copy_image_for_circle_dot_counting=roi_black_and_white.copy()
                        center = ((ex + efx) // 2, (ey + efy) // 2)
                        radius = int(np.sqrt((efx - ex)**2 + (efy - ey)**2) // 2)
                        cv2.circle(copy_image_for_circle_dot_counting, center, radius, (255, 0, 0), -1)                     
                        for y in range(height):
                            for x in range(width):
                                if (copy_image_for_circle_dot_counting[y,x]==[255,0,0]).all():
                                    erase_point_list.append((x,y))
                        
                        for y in range(height):
                            for x in range(width):
                                if tix<x<tfx and tiy<y<tfy:
                                    roi_black_and_white[y,x]=255,255,255
                                    if y % scale_fact == 0 and x % scale_fact == 0 :
                                        subset_vector_points_list.append((x,y))
                                elif ix<x<fx and iy<y<fy:
                                    roi_black_and_white[y,x]=255,255,255
                        
                        set1=set(subset_vector_points_list)   
                        set2=set(erase_point_list)      
                        
                        # set2 = set(tuple(x) for x in erase_point_list)
                        common=set1.intersection(set2)
                        result=[element for element in subset_vector_points_list if element not in common ]
                        
                        for ind,val in enumerate(result):
                            x,y=val
                            cv2.line(image,(x,y), (x, y), (0,0, 255), 4)
                        
                        
                        for ind,val in enumerate(erase_point_list):
                                x,y=val    
                                roi_black_and_white[y,x]=0,0,0
                                
                    elif mode=="free-form":
                        None
                    
            elif erase==False:
                subset_vector_points_list=[]
                for y in range(height):
                    for x in range(width):
                        if tix<x<tfx and tiy<y<tfy:
                            roi_black_and_white[y,x]=255,255,255
                            if y % scale_fact == 0 and x % scale_fact == 0 :
                                subset_vector_points_list.append((x,y))
                                cv2.line(image,(x,y), (x, y), (0,0, 255), 4)
                        elif ix<x<fx and iy<y<fy:
                            roi_black_and_white[y,x]=255,255,255
            return image,roi_black_and_white
        
        
        img_temp=image.copy()
        # Start drawing on left mouse button event
        drawing = False
        
        # Define starting and ending points for line
        ax, ay = -1, -1
        mode="rectangle"
        def draw_shape(event, x, y, flags, param):
            global afx,afy,ax, ay,drawing,roı_check,area
            if event == cv2.EVENT_LBUTTONDOWN:
                drawing = True
                ax, ay = x, y
            
            elif event == cv2.EVENT_MOUSEMOVE:
                if drawing == True:
                    image[:] = img_temp
                    
                    if mode=="rectangle":
                        cv2.rectangle(image, (ax, ay), (x, y), (0, 255, 255), 2)
                    
                    elif mode=="circle":
                        center = ((ax + x) // 2, (ay + y) // 2)
                        radius = int(np.sqrt((x - ax)**2 + (y - ay)**2) // 2)
                        cv2.circle(image, center, radius, (0, 255, 255), 2)
                    elif mode=="free-form":
                        None
                    else:None  
        
            elif event == cv2.EVENT_LBUTTONUP:
                # image[:] = img_temp
                drawing = False
                rect_area=[]
                circle_area=[]
                form_area=[]
                # area4=[]
                if kayıt==True:
                    
                    if mode=="rectangle":
                        afx,afy=x,y
                        rectangles.append([ax,ay,afx,afy])
                        rect_area=kordinat_solvır(mode,rectangles=rectangles,kayıt=kayıt)
                        
                        for i,v in enumerate(rectangles):
                            ix,iy,ifx,ify=v
                            cv2.rectangle(image, (ix, iy), (ifx, ify), (0, 255, 255), 2)
                            
                    elif mode=="circle":None
                        # circle_area=[]
                    elif mode=="free-form":None
                        # form_area=[]
                    else:None
                        # area4=[]
                    
                    subset_point_drawer(image, scale_fact,erase=True,
                                        mode=mode,kayıt=True,rect_area=rect_area,
                                        circle_area=circle_area,form_area=form_area)
                elif kayıt==False:
                    
                    if mode=="rectangle":
                        cv2.rectangle(image, (ax, ay), (x, y), (0, 255, 255), 2)
                        
                    elif mode=="circle":
                        center = ((ax + x) // 2, (ay + y) // 2)
                        radius = int(np.sqrt((x - ax)**2 + (y - ay)**2) // 2)
                        cv2.circle(image, center, radius, (0, 255, 255), 2)
                    elif mode=="free-form":None
                    else:None
                    
                    afx,afy=x,y
                    area=kordinat_solvır(mode,ax,ay,afx,afy,kayıt=kayıt)
                    subset_point_drawer(image, scale_fact,erase=True,mode=mode,kayıt=False,area=area)
        
        rectangles=[]       
        area_rectangles=[]  
        global rect_count
        rect_count=0
        def kordinat_solvır(mode,ax=None,ay=None,afx=None,afy=None,rectangles=None,kayıt=False):
            global rect_count
            area=[]
            global eraser_dec
            eraser_dec=True
            
            def dikelten(ax,ay,afx,afy):
                if mode=="rectangle":
                    if ax>afx and ay<afy:   #Sol alt
                        iix,ifx=afx,ax
                        ax=iix
                        afx=ifx
                        area=[ax,ay,afx,afy]
                    elif ax>afx and ay>afy: #Sol üst
                        iix,ifx=afx,ax
                        iiy,ify=afy,ay
                        ax=iix
                        afx=ifx
                        ay=iiy
                        afy=ify
                        area=[ax,ay,afx,afy]
                    elif ax<afx and ay>afy: #Sağ üst
                        iiy,ify=afy,ay
                        ay=iiy
                        afy=ify
                        area=[ax,ay,afx,afy]
                    elif ax<afx and ay<afy: #Sağ alt
                        area=[ax,ay,afx,afy]
                elif mode=="circle":
                    
                    if ax>afx and ay<afy:   #Sol alt
                        iix,ifx=afx,ax
                        ax=iix
                        afx=ifx
                        area=[ax,ay,afx,afy]
                    elif ax>afx and ay>afy: #Sol üst
                        iix,ifx=afx,ax
                        iiy,ify=afy,ay
                        ax=iix
                        afx=ifx
                        ay=iiy
                        afy=ify
                        area=[ax,ay,afx,afy]
                    elif ax<afx and ay>afy: #Sağ üst
                        iiy,ify=afy,ay
                        ay=iiy
                        afy=ify
                        area=[ax,ay,afx,afy]
                    elif ax<afx and ay<afy: #Sağ alt
                        area=[ax,ay,afx,afy]
                elif mode=="free-form":
                    None
                else:
                    None
                return area
                    
            if mode=="rectangle":
                if kayıt==True:
                    # for i,v in enumerate(rectangles):
                    
                    ax,ay,afx,afy=rectangles[rect_count]
                    rect_count+=1
                    area=dikelten(ax, ay, afx, afy)
                    area_rectangles.append(area)
                    area=area_rectangles
                        
                elif kayıt==False:
                    area=dikelten(ax, ay, afx, afy)

            elif mode=="circle":
                # Circle İçinde Üsteki gibi eklenmeli imalat yapılacak
                
                if ax>afx and ay<afy:   #Sol alt
                    iix,ifx=afx,ax
                    ax=iix
                    afx=ifx
                    area=[ax,ay,afx,afy]
                elif ax>afx and ay>afy: #Sol üst
                    iix,ifx=afx,ax
                    iiy,ify=afy,ay
                    ax=iix
                    afx=ifx
                    ay=iiy
                    afy=ify
                    area=[ax,ay,afx,afy]
                elif ax<afx and ay>afy: #Sağ üst
                    iiy,ify=afy,ay
                    ay=iiy
                    afy=ify
                    area=[ax,ay,afx,afy]
                elif ax<afx and ay<afy: #Sağ alt
                    area=[ax,ay,afx,afy]
            elif mode=="free-form":
                None
            else:
                None
            return area
        
        cv2.namedWindow('Select Subsset Space')
        cv2.imshow('Select Subsset Space', image)
        cv2.setMouseCallback('Select Subsset Space', draw_shape)
        eraser_dec=False
        kayıt=False
        
        image[:] = img_temp
        image,roi_black_and_white=subset_point_drawer(image,scale_fact,erase=eraser_dec)
        while(1):
            
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('+'):
                mode="rectangle"
                rectangles=[]
                area_rectangles=[]
                eraser_dec=False
                image[:] = img_temp
                scale_fact=scale_fact+1
                print("Subset Spacing:",scale_fact)
                image,roi_black_and_white=subset_point_drawer(image,scale_fact,erase=eraser_dec)
            
            elif key == ord('-'):
                mode="rectangle"
                rectangles=[]
                area_rectangles=[]
                eraser_dec=False
                image[:] = img_temp
                ref_scale_fact=scale_fact
                scale_fact=scale_fact-1 
                if scale_fact<=0:
                    scale_fact=ref_scale_fact
                print("Subset Spacing:",scale_fact)
                image,roi_black_and_white=subset_point_drawer(image,scale_fact,erase=eraser_dec)
                
            elif key == ord('x'):
                mode="rectangle"
                kayıt=False
                rectangles=[]
                area_rectangles=[]
                eraser_dec=False
            
                image[:] = img_temp
                scale_fact=10
                image,roi_black_and_white=subset_point_drawer(image,scale_fact,erase=eraser_dec)
                
            elif key == ord('r'):#Rectangle
                mode="rectangle"
                # image[:] = img_temp
                print(mode)
            elif key == ord('c'):#Circle
                mode="circle"    
                # image[:] = img_temp
                print(mode)
            elif key == ord('f'):#FreeForm
                mode="free-form"    
                print(mode)
                # image[:] = img_temp
            elif key == ord('s'):#Rectangle
                if kayıt==True:
                    kayıt=False
                elif kayıt==False:
                    kayıt=True
                
                # print(kayıt)
            elif key == 27:
                
                if mode=="rectangle" or mode=="circle" or mode=="free-form":
                    eraser_dec=True
                    image[:] = img_temp
                    image,roi_black_and_white=subset_point_drawer(image,scale_fact,erase=eraser_dec,mode=mode,area=area)
                else:
                    eraser_dec=False
                    image[:] = img_temp
                    image,roi_black_and_white=subset_point_drawer(image,scale_fact,erase=eraser_dec)
                break
            
            # image,roi_black_and_white=subset_point_drawer(image,scale_fact,erase=eraser_dec)
            
            '''
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            font_scale = 1
             
            font_color = (255, 255, 255)
            
            text_start = (10, 30)
            
            # Define the text to be written
            text = f"Subset Spacing:{scale_fact}!"
            cv2.putText(image, text, text_start, font, font_scale, font_color, thickness=2)'''

            cv2.rectangle(image,(snix,sniy),(snfx, snfy),(255, 0,0), 2)
            cv2.imshow("Select Subsset Space", image)
            
        cv2.destroyAllWindows()
        cv2.imshow("roi_black_and_white", roi_black_and_white)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
                
        cv2.rectangle(image,(ix,iy), (fx,fy),  (0, 255,0), 2)
        cv2.rectangle(image,(snix,sniy), (snfx, snfy),(255, 0,0), 2)
        # Show the image
        cv2.imshow("Subset Area", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("ss.tif",image)
        
    except Exception as e:
        print(e)
        pass
#%%
# print(8)
#%% Run of Vector_Positions

vector_positions(img,pre_vector_list)   

#%%
# print(9)
#%%


#%%
# list_of_images=image_folder_handler()
# img_loader(list_of_images)
    

