"""
Vi ska så småningom arbeta med tkinter bibliotek som används för grafisk visning av olika funktioner. Studera följande kod och försök att
förstå vad den gör. Jag rekommenderar att ni självklart kör koden först:
"""

from tkinter import *
from tkinter import ttk
 
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
 
    def create_widgets(self):
        self.button = Button(self, text = "Click me!", command = self.click)
        self.button.grid()
 
        self.text = Text(self, width = 40, height = 5, wrap = WORD)
        self.text.grid()
 
    def click(self):
        self.text.insert(0.0, "You clicked the button!\n") #add new line when button click
 
root = Tk()
 
root.title("Click me!")
 
app = Application(root)
 
root.mainloop()