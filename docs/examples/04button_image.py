'''
Image on Button

Use png image files, if running tkinter 8.6 or more, this will run - if using tkinter 8.5 then we  need to use
PIL open the images with PIL.Image then load this with ImageTk.PhotoImage into the Button widget.

The image needs to be referred to if the handle is a local variable, otherwise use a class variable (prefixed with self)
'''
from tkinter import Tk, PhotoImage, Frame
from tkinter.ttk import Button, Style
#from PIL import Image, ImageTk ## uncomment if you are running tkinter 8.5
# if tkinter 8.6 or greater PIL no longer needed

class Example:
    def __init__(self, master):
        fr = Frame(master) 
        master.title('Button Test')
        fr.grid(column=0, row=0, sticky=('nsew'))
        ## uncomment following 4 lines if you are running tkinter 8.5
        # im1 =  = Image.open('../images/butImage.png') ##
        # im2 = Image.open('../images/butImageTrans.png') ##
        # self.buttonPhoto = ImageTk.PhotoImage(im1)  ##
        # buttonPhotoTrans = ImageTk.PhotoImage(im2)  ##
        
        ## comment out following 2 lines if you are running tkinter 8.5
        self.buttonPhoto = PhotoImage(file='../images/butImage.png') ##
        buttonPhotoTrans = PhotoImage(file='../images/butImageTrans.png') ## 
        '''
        we are using both a local and a variable prefixed with self
        '''
        but = Button(master, image=self.buttonPhoto)
        #but.image = self.buttonPhoto - not needed because using self
        but.grid(column=0, row=0, sticky=('ew'), padx=10, pady=10)
        myButton = Button(master, compound='center', text='Click on Me!',
                         style='new.TButton', image=buttonPhotoTrans) 
        myButton.image = buttonPhotoTrans # keep a reference as local variable!
        myButton.grid(column=0, row=1, sticky=('ew'), padx=10, pady=10)
        myButton2 = Button(master, compound='center', 
                           text='Really long now - Click on Me!',
                         style='new.TButton', image=buttonPhotoTrans) 
        myButton2.image = buttonPhotoTrans # keep a reference as local variable!
        myButton2.grid(column=0, row=2, sticky=('ew'), padx=10, pady=10)

if __name__ == "__main__":
    root = Tk()
    s=Style()
    s.theme_use('default') # ensure all see the same
    # produce a large heavy text, 
    s.configure('new.TButton',font='Helvetica 20 bold') 
    # button font does not work in tkinter 8.6
    example = Example(root)
    root.mainloop()
