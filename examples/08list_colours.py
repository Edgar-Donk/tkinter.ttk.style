from PIL import Image
from pprint import pprint

def getKey(item):
    return sum(item[-1])
sourceFile = '../images/comboarrow-n.gif'
img = Image.open(sourceFile)
cols = img.convert('RGB').getcolors()
# sorting by sum of rgb values
pprint(sorted(cols,key=getKey))
