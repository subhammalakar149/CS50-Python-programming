# Blurs an image
#imports modules Image & ImageFilter from lib called PIL. This takes an input file & creates an output file
from PIL import Image, ImageFilter

# Blur image
before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("out.bmp")
