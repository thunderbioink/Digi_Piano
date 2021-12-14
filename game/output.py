"""
- Description:
   
    In this class image objects will be displayed on the screen object when calling this class 
    in main. It prints out your screen and keynote actors. 
    
    In __main__, the code that accesses the Output class looks like this:
    'output_service = Output(actor)' - you call your base actor (screen) on where you want to
    display your keynote actors.
    Print each keynote with:
    'output_service.draw(actor)'
    
- OOP Principles Used:
   Abstraction.

- Reasoning:
    This class uses Abstraction because it takes the preset private methods for image, and 
    actor(x,y) to print out an actor. It takes something that's completly shapeless
    and turns it into something physical: our actors. But you don't need to know all this happens
    here, all you need to do is call output_service.draw(Actor) and you just print out a keynote object!
"""
class Output():
    
    def __init__(self, screen):
        
        self._screen = screen
    
    def draw (self, actor):
        self._screen.blit(actor.get_image(), actor.x_and_y())
        
        
        