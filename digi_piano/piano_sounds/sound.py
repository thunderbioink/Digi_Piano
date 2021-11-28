from tkinter import*
import time
import datetime
import pygame


pygame.init()
root=Tk()
root.title("Digi Piano")
root.geometry("1352x700+0+0")
root.configure(background = "white")

ABC = Frame(root, bg = "powder blue", bd = 20, relief = RIDGE )
ABC.grid()
ABC1 = Frame(root, bg = "powder blue", bd = 20, relief = RIDGE )
ABC1.grid()
ABC2 = Frame(root, bg = "powder blue", bd = 20, relief = RIDGE )
ABC2.grid()
ABC3 = Frame(root, bg = "powder blue", bd = 20, relief = RIDGE )
ABC3.grid()


root.mainloop()
