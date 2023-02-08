# VIQUAC

Virtual Qualitiy Assessment for Composites (VIQUAC) is a software that determines the volume fraction of fiber or resin 
and calculates the mechanical behavior of the material by Classical Lamination Theory (CLT).


## Libraries
-Tkinter  
-NumPy  
-OpenCV   
-Sqlite3    
-OpenPyxl   
-Matplotlib   
-imea   
-OS, Math, re

Were used in VIQUAC.

## Basic Methodology
  Using the image processing methods to predict quality assessment of composite materials and predict the mechanical behavior according to Classical Lamination Theory(CLT).
##### Work FLow  

1.  User must input an image to GUI by selecting the Browse File Button.  
2.  To determine Volume Fraction(Vf), user must select the Volume Fraction Button.  
    -After selecting the Vf button, OpenCV window will occur.   
    -User must known that fibers or resin discriminates by its color difference. So, if the fibers are more lighter then resin fibers will be assigned as red color.    
    -If this situation is vice-versa, then please select black-kind of fibers checkbutton to avoid from the issues.       
    
    2.1.On the window, Brightness, Red Area Ratio and Contrast Scale Bars will shown respectievly.    
    2.2.Please select the correct ratios by hand while looking.   
    2.3.When you select Fibers, please press Escape button to Close window. Otherwise, OpenCV will Crash.   
    If you have an image already saved by VIQUAC it will pop-up a windows that tells you to make new determination.
3.  Select Calculator Button to start calculation process.    
  -After selecting the button, pop-up window will show itself.    
  -Select Fiber and Resin Type For your application and predict the mechanical behavior.    
  -If you decided which kinds of fiber and resin that will use, please select confirm button.
