"""
- Description:
   
    The following class (parent class for Keys class) creates private parameters for the keynote objects in __main__:
    Each keynote will have an assigned image path, with x and y values.


- OOP Principles Used:
   Encapsulation.

- Reasoning:
    This class uses Encapsulation because it contains the private parameters that
    are used to call the image and x and y values for each keynote(actor). Without these private parameters,
    we don't have a reference for our Output class(which needs these private parameters to print out
    the image objects) and our Keys class(which inherits from it and returns them as methods). This class is 
    the box that contains the file name for each keynote, without having to copy and paste the image paths over
    and over again. This class is also the box that contains the x and y position base, so when the user wants to 
    specify the x y methods with the Key class, they can; all that because of the Actor class!
    
    Encapsulation is one of the OOP that helps you avoid copying pasting long lines of code. 
"""
class Actor():
    #Base class , no inheritance: 
    def __init__(self, image, x,y):
    
        self._image = image
        self._x = x
        self._y = y 
        
    #Parameters in __init__ need to be private, I need methods that call these attributes
    #in other functions.
    def get_image(self):
        
        return self._image
    #Set_x & set_y function:
    def x_and_y (self):
        # This is encapsulation
        return self._x, self._y
    
    