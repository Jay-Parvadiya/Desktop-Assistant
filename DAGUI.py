
from tkinter import *
from PIL import Image

root = Tk()

root.geometry('250x470')
root.configure(background='Black')

gifImage = "giphy.gif"

openImage = Image.open(gifImage)

frames = openImage.n_frames
imageObject = [PhotoImage(file=gifImage,format=f'gif -index {i}') for i in range(frames)]

count = 0
showAnimation = None

def animation(count):
    global showAnimation
    newImage = imageObject[count]

    gif_label.configure(image=newImage)
    count +=1
    if count == frames:
        count = 0
    showAnimation = root.after(50,lambda:animation(count))


gif_label = Label(root,image="")
gif_label.place(x=-5,y=0,width=400,height=400)
animation(count)

# root.geometry("x675")
root.minsize(395,460)
root.maxsize(395,460)
root.resizable(False,False)
root.config(bg="#fcfcfc")
# Set the window to be always on top (ensure compatibility)
try:
    root.attributes('-topmost', True)  # Try Tkinter approach first
except Tk.TclError:
    try:
        root.wm_attributes('-topmost', True)  # Try wm_attributes if necessary
    except Exception as e:
        print("Error setting 'always on top':", e)
        
text=Text(root,font = ('courier 10'),bg="#000000",borderwidth=3,relief=SOLID,fg='#fcfcfc')
text.grid(row=2,column=0)
text.place(x=0,y=365,width=400,height=100)

def guiStart(nothing):
    root.mainloop()

if __name__ == "__main__":
    
    guiStart("self")
    