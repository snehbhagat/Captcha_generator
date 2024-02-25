from PIL import Image,ImageDraw
img = Image.new('RGB',(90,60),color = 'white')
draw = ImageDraw.Draw(img)
draw.text((20,20),"Hello World",fill=(38,38,38))
draw.line(((30,15),(50,150)),fill=100,width=1)
draw.point(((30,40),(90,33),(20,56),(10,50),(30, 40), (10, 20), (14, 25), (35, 10), (14, 28), (17, 25)),fill="black")
img.save('blank_image.png')