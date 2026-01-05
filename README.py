# businessSolution_textEditor2
from tkinter import *
from tkmacosx import Button
root = Tk()
root.title("Note Solution for Business Problem")
root.geometry("1000x750")
whitebutton = Button(root, text="Click to start audio note catching", width=300, height = 100)
whitebutton2 = Button(root, text="Click here to start manual note catching", width=300, height=100)
whitebutton3 = Button(root, text="Click here to extract saved notes file", width=300, height=100)



whitebutton.grid(row=1, column=5, padx=400, pady=10)
whitebutton2.grid(row=2, column=5, padx=400 ,pady=10)
whitebutton3.grid(row=3, column=5, padx=400, pady=10)







root.mainloop()