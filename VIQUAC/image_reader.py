import cv2 as cv
import numpy as np
def average_color(file_name):
    try:
        if isinstance(file_name, np.ndarray):
            img=np.copy(file_name)
            img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        else:
            img=cv.imread(file_name)
            img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        
        average_color_row = np.average(img, axis=0)
        average_color = np.average(average_color_row, axis=0)
        return average_color,img 
    except Exception as e:
        print(e)