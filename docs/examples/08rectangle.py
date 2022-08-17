# Simple Rectangle
from PIL import Image, ImageDraw

e = 9 # enlargement, also thickness between rectangles
w,h = 23, 23
we,he = w*e,h*e

def create_rectangle(size, outline, fill):
    width, height = size
    box = 0, 0, width-1, height-1
    # adjust the size of the rectangle to suit the image size
    rect = Image.new('RGBA', size, fill)
    draw = ImageDraw.Draw(rect)
    draw.rectangle(box, fill=outline) # The outer rectangle
    draw.rectangle( # The inner rectangle
        (box[0] + e, box[1] + e, box[2] - e, box[3] - e),
        fill=fill)
    return rect

inp = create_rectangle((we,he), "blue", "white")
inp.save('../figures/08rect.png')