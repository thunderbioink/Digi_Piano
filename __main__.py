"""
- Description:
   
    In this file all classes and libraries are imported, to run the game smoothly:
    pygame being our superstar. We were able to distribute a called method from pygame
    into the Output class, known as blit. This method is the most important to see each
    keynote actor.
    
    Our sounds are their own separate set of actors, that inherit the x,y positions from
    the keynote actors, in the lower FOR EVENT loop and play each time a specific keynote is
    clicked on a specfic set of defined pixels.
    
- OOP Principles Used:
   Polymorphism and Inheritance.

- Reasoning:
    This file uses Polymorphism and Inheritance because it reuses the parameters and attributes logic in all
    our predefined classes and libraries. In this file, polymorphism takes shape in the FOR EVENT loop, when
    a sound is called, it is only able to play if it takes the same pixel values assigned to each given Keynote
    actor. Eeach sound actor can only play if set under each clickable asigned pixel. You don't need the argument
    to play a sound in that loop repeated over again. You only need it once per each keynote. 
"""
# Abstraction and Polymorphism can work together.
import pygame
from game.keys import Keys
from game.output import Output
from pygame import mixer
# Initialize pygame
pygame.init()
mixer.init()
# Game screen
screen = pygame.display.set_mode((675,450))

# Loading Background & Piano Key images
background = pygame.image.load('game\images\_background.jpg')
white_key = pygame.image.load('game\images\white_key.jpg')
black_key = pygame.image.load('game\images\sharp_key.png')

output_service = Output(screen)
# While loop for the game to initialize: True until False == Quit:
running = True
# While loop opens:
while running:
    #Screen Fill - Black, Underneath Background:
    screen.fill((0,0,0))
    # Background Image:
    screen.blit(background, (750,450))
    
    
    
    sound_C3 = pygame.mixer.Sound('game\piano_sounds\C3 61 key Piano.wav')
    sound_Db3 = pygame.mixer.Sound('game\piano_sounds\C3 Sharp & D3 Flat.wav')
    sound_D3 = pygame.mixer.Sound('game\piano_sounds\D3 61 key Piano.wav')
    sound_Eb3 = pygame.mixer.Sound('game\piano_sounds\D3 Sharp & E3 Flat.wav')
    sound_E3 = pygame.mixer.Sound('game\piano_sounds\E3 61 key Piano.wav')
    sound_F3 = pygame.mixer.Sound('game\piano_sounds\F3 61 key Piano.wav')
    sound_Gb3 = pygame.mixer.Sound('game\piano_sounds\F3 Sharp & G3 Flat.wav')
    sound_G3 = pygame.mixer.Sound('game\piano_sounds\G3 61 key Piano.wav')
    sound_Ab3 = pygame.mixer.Sound('game\piano_sounds\G3 Sharp & A3 Flat.wav')
    sound_A3 = pygame.mixer.Sound('game\piano_sounds\A3 61 key Piano.wav')
    sound_Bb3 = pygame.mixer.Sound('game\piano_sounds\A3 Sharp & B3 Flat.wav')
    sound_B3 = pygame.mixer.Sound('game\piano_sounds\B3 61 key Piano.wav')
   

    #Draw in output - an abstraction - Key inherits from Actor:
    c3 = Keys(white_key, 0,0)
    C3 = output_service.draw(c3)
    db3 = Keys(black_key, 50,-500)
    Db3 = output_service.draw(db3)
    d3 = Keys(white_key, 100,0)
    D3 = output_service.draw(d3)
    eb3 = Keys(black_key, 150,-500)
    Eb3 = output_service.draw(eb3)
    e3 = Keys(white_key, 200,0)
    E3 = output_service.draw(e3)
    f3 = Keys(white_key, 300,0)
    F3 = output_service.draw(f3)
    gb3 = Keys(black_key, 350,-500)
    Gb3 = output_service.draw(gb3)
    g3 = Keys(white_key, 400,0)
    G3 = output_service.draw(g3)
    ab3 = Keys(black_key, 450,-500)
    Ab3 = output_service.draw(ab3)
    a3 = Keys(white_key, 500,0)
    A3 = output_service.draw(a3)
    bb3 = Keys(black_key, 550,-500)
    Bb3 = output_service.draw(bb3)
    b3 = Keys(white_key, 600,0)
    B3 = output_service.draw(b3)
    
    width = screen.get_width()
    height = screen.get_height()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #The variable mouse is a tuple:
            mouse = pygame.mouse.get_pos()
            
            # BLACK KEYS - clickable areas:
            
            if 50 <= mouse[0] <= 100 and 0 <= mouse[1] <= 250:
                sound_Db3.play()
                print("db3")
            elif 150 <= mouse[0] <= 200 and 0 <= mouse[1] <= 250:
                sound_Eb3.play()
                print("eb3")
            elif 350 <= mouse[0] <= 400 and 0 <= mouse[1] <= 250:
                sound_Gb3.play()
                print("gb3") 
            elif 450 <= mouse[0] <= 500 and 0 <= mouse[1] <= 250:
                sound_Ab3.play()
                print("ab3")
            elif 550 <= mouse[0] <= 600 and 0 <= mouse[1] <= 250:
                sound_Bb3.play()
                print("bb3")
            #WHITE KEYS - clickable areas:
            elif 0 <= mouse[0] <= 100 and 0 <= mouse[1] <= 1198:
                sound_C3.play()
                print("C3") 
            elif 100 <= mouse[0] <= 200 and 0 <= mouse[1] <= 1198:
                sound_D3.play()
                print("D3")
            elif 200 <= mouse[0] <= 300 and 0 <= mouse[1] <= 1198:
                sound_E3.play()
                print("E3")
            elif 300 <= mouse[0] <= 400 and 0 <= mouse[1] <= 1198:
                sound_F3.play()
                print("F3")
            elif 400 <= mouse[0] <= 500 and 0 <= mouse[1] <= 1198:
                sound_G3.play()
                print("G3")
            elif 500 <= mouse[0] <= 600 and 0 <= mouse[1] <= 1198:
                sound_A3.play()
                print("A3")
            elif 600 <= mouse[0] <= 700 and 0 <= mouse[1] <= 1198:
                sound_B3.play()
                print("B3")
                
    pygame.display.update()


