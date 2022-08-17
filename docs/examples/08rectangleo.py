# Simple Rectangle
from PIL import Image, ImageDraw

e = 9 # enlargement, also thickness between rectangles
w,h = 16, 24
we,he = w*e,h*e

def create_rectangle(size, outer, border, background, thick):
    wi,ht = size
    box = 0, 0, wi-1, ht-1
    # adjust the size of the rectangle to suit the image size
    rect = Image.new('RGBA', (wi, ht), (0, 0, 0, 0))
    draw = ImageDraw.Draw(rect)
    draw.rectangle(box, fill=outer) # The outer rectangle
    draw.rectangle( # The border rectangle
        (box[0] + thick, box[1] + thick, box[2] - thick, box[3] - thick),
        fill=border)
    draw.rectangle( # The background rectangle
        (box[0] + 2*thick, box[1] + 2*thick, box[2] - 2*thick, box[3] - 2*thick),
        fill=background)
    return rect

inp = create_rectangle((we,he), "lightblue", "blue", 'white', e)
inp.save('rect.png')