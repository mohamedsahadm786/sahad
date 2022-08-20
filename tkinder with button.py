from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("MOHAMED")
window.configure(bg="#AF33FF")

def butt():
    print("button clicked.")
button = Button(window,text= "sahad",command= butt)



button.pack()


window.mainloop()
print("hi")