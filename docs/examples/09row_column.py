from PIL import Image
im = Image.open('../images/')
# cl_button-n.png elegance_button-default.gif
im.convert(RGBA)
'''
pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
'''
pixels = im.load() # this is not a list
width, height = im.size
row_averages = []
for y in range(2,height-3): #2,height-2
    cur_row_ttl = 0
    for x in range(6,width-7): # 2,width-3
        cur_pixel = pixels[x, y]
        cur_pixel_mono = sum(cur_pixel) / len(cur_pixel)
        cur_row_ttl += cur_pixel_mono

    #cur_row_avg = round(cur_row_ttl / (width - 4),2)
    #row_averages.append(cur_row_avg)

print('rows')
print (row_averages)

col_averages = []
for x in range(6,width-7): #2,width-2
    cur_col_ttl = 0
    for x in range(2,height-3): # 2,height-3
        cur_pixel = pixels[x, y]
        cur_pixel_mono = sum(cur_pixel) / len(cur_pixel)
        cur_col_ttl += cur_pixel_mono

    #cur_col_avg = round(cur_col_ttl / (height - 4),2)
    #col_averages.append(cur_col_avg)

print('cols')
print (col_averages)
