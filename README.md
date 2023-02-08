# VIQUAC

Virtual Quality Assessment for Composites (VIQUAC) is a software that determines the volume fraction of fiber or resin 
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
## Run  

1.  User must input an image to GUI by selecting the Browse File Button.  
2.  To determine Volume Fraction(Vf), the user must select the Volume Fraction Button:    
    -After selecting the Vf button, the OpenCV window will occur.   
    -User must know that fibers or resin discriminate by its color difference. So, if the fibers are lighter then resin fibers will be assigned as red color.    
    -If this situation is vice-versa, then please select black-kind of fibers check button to avoid the issues.       
    
    2.1.On the window, Brightness, Red Area Ratio, and Contrast Scale Bars will be shown respectively.    
    2.2.Please select the correct ratios by hand while looking.   
    2.3.When you scan Fibers with red, please press the "Escape" button to Close the window. Otherwise, OpenCV will Crash.   
    If you have an image already saved by VIQUAC it will pop-up a window that tells you to make a new determination or continue with saved file.
3.  Select the Calculator Button to start the calculation process:    
  -After selecting the button, the pop-up window will show itself.    
  -Select Fiber and Resin Type For your application and predict the mechanical behavior.    
  -If you decided which kinds of fiber and resin you will use, please select confirm button.
4. All the process is finsihed. Files are saved in "Save_File" with their own names.

