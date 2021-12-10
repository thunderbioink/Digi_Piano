class Actor():
    #Base class , no inheritance
    """
    This class creates parameters for the key objects in __main__:
    Each keynote will have an image, and an x and y position.
    
    Avoid doing unnecessary copy/paste for the image path for each key.
    
    """ 
    def __init__(self, image, x,y):
    
        self._image = image
        self._x = x
        self._y = y 
        
    #Parameters in __init__ need to be private, I need methods that call these attributes
    #in other functions.
    def get_image(self):
        
        return self._image
    #set_x set_y
    def x_and_y (self):
        # this is encapsulation
        return self._x, self._y
    
    