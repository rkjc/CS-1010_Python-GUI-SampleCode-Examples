 
from PIL import Image


imgPath = 'kitten.jpg'
img = Image.open(imgPath)

print('The format of img is: ', img.format)
print('The mode of img is: ', img.mode)
print('The size of img is: ', img.size)
print('The palette of img is: ', img.palette)
