from PIL import Image, ImageDraw
'''
alternative arrow following classic theme

The option to draw larger then reduce with filter is given.
On larger drawing a circle at the mid point can be made.
'''

# create circle with centre and radius
def create_circle(idraw,c,r,outline='#888888',fill='#888888'):
    return idraw.ellipse([c[0]-r,c[1]-r,c[0]+r-1,c[1]+r-1],
                          outline=outline,fill=fill)
e=1 # enlargement use 9
width = 13
height = 12
mid = 4
back = 'white'
img = Image.new('RGBA', (width*e,height*e), back)
idraw = ImageDraw.Draw(img)

idraw.polygon([0,0,(width-1)*e/2,mid*e,(width-1)*e,0],fill='#76eec6')
idraw.polygon([0,0,(width-1)*e/2,(height-1)*e,(width-1)*e/2,mid*e],
              fill='lightgreen')
idraw.polygon([(width-1)*e,0,(width-1)*e/2,(height-1)*e,(width-1)*e/2,mid*e],
              fill='green')
#create_circle(idraw,[(width-1)*e/2,mid*e],1*e,fill='chartreuse')

#img.save('class_arrx.png')
#img = img.resize((width,height), Image.LANCZOS)

#img.save('class_arro'+str(e)+'.png')
img.show()

