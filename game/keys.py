"""
- Description:
   
    In this class (child class of Actor class), actors will be defined in __main__ the folloing way:
    actor = Keys(image, x,y)
    
    For our program our actors are all unique keynotes in a digital piano,
    so it'll be important that all keynotes are labeled uniquely to be called
    and later printed out with the Output class.
    
- OOP Principles Used:
   Inheritance.

- Reasoning:
    This class uses Inheritance because it reuses the parameters and attributes logic in the Actor
    class. Remember how in Actor class I explained that? Well, now that we're seeing it, each time we want
    to Output(print out) an Actor (each keynote), before using our output_service, we'll have to pick the image
    variable and it's x and y position values. The Keys class has shared superpowers from Actor. 
"""
from game.actor import Actor

# Keys needs to inherit from Actor
class Keys(Actor):
        pass
    