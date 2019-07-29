'''
progressbar

Standard gradient on vertical to create 90° gradient to normal

'''
from PIL import Image
from roundrect import Gr_Base_Rect

exp = 9 # enlargement, also thickness between rectangles
w=17
h=21

radius = 4 # gap size

first = '#2D4C46' #(222,247,222) '#5D9B90' 5F9C8E
second = 'white' #(102,153,204)

startc = (143,188,143) #(222,247,222) (26,242,195)
stopc = (95,156,142)#(143,188,143)(222,247,222) (225,242,238)

tab=0
fout = '../images/lime/vprog.png' 

Gr_Base_Rect(fout,w,h,exp,radius,first,second,startc,stopc,tab)
          
img = Image.open('../images/lime/vprog.png')

img.transpose(Image.ROTATE_90).save('../images/lime/hprog.png')


