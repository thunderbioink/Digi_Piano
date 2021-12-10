class Output():
    """
    User will get object displayed on screen.
    ABSTRACTION
    """
    def __init__(self, screen):
        
        self._screen = screen
    
    def draw (self, actor):
        self._screen.blit(actor.get_image(), actor.x_and_y())
        
        
        