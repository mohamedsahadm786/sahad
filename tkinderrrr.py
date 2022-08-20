from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("MOHAMED")
# window.geometry("500x500") - for setting the size of the window.
window.configure(bg="#AF33FF")
# window.configure(bg="yellow") - means we get yellow colour as the window colour.
# #AF33FF - we get this from 'html colour code' in google.
button = Button(window,text= "sahad",width= 30,height= 30,bg= "red",fg= "white")
""" here width and height are equal.that is 30.but the output length is different.bcz here the length means- if we put 
30 then it taken the length of 30 zeros ,that set horizontally (width) or vertically (height). 
"""

label = Label(window,text="welcome")
button.pack()
label.pack()

window.mainloop()
print("hi")