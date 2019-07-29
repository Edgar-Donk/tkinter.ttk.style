from PIL import Image, ImageDraw

e = 9 # enlargement, also thickness between rectangles
d = (e-1)//2 # displacement
w=15
h=15
we = w*e  
he = h*e
back = 'white'
farb = (191,191,191) #(127,127,127)

img = Image.new('RGB', (we,he), back)
idraw = ImageDraw.Draw(img)

idraw.line([d,3*e,d,he-4*e],fill=farb,width=e)
idraw.line([we-d-e-1,3*e,we-d-e-1,he-4*e],fill=farb,width=e)

img = img.resize((w,h),Image.LANCZOS)
img.save('../figures/09test_filt2.png')
