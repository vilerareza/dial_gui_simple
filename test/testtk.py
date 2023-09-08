from tkinter import *
from threading import Thread
from PIL import ImageTk as itk
from PIL import Image

root = Tk()
root.geometry('600x600')
root.title('test')

#img = PhotoImage(file = 'images/dialer.png')
img_pil = Image.open('images/dialer.png').rotate(90)

img = itk.PhotoImage(img_pil)
canvas = Canvas(background='black', width='300', height='300')
canvas.image = img
canvas.create_image(0,0, image = img)#, anchor ='center')
canvas.pack()
#print (canvas.image.angle)
#lbl = Label(image = img)
#lbl.pack()

#root.mainloop()

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return

root.bind('<B1-Motion>',motion)
#root.bind('<Button>', '<Motion>',motion)
root.mainloop()