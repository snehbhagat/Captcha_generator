from PIL import Image,ImageDraw
img = Image.new('RGB',(90,60),color = 'white')
img.save('blank_image.png')
draw = ImageDraw.Draw(img)
draw.text((20,20),"Hello World",fill=(38,38,38))
img.save('blank_image.png')
