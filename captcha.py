from PIL import Image, ImageDraw, ImageFont
import string, random

def generate_string():
    n = 5
    char_set = string.ascii_letters
    ran_str = ''.join(random.choices(char_set, k=n))
    return ran_str

get_location = lambda: (random.randrange(5, 200), random.randrange(5, 100))

img = Image.new('RGB', (200, 100), color='white')
draw = ImageDraw.Draw(img)

draw.line((40, 30, 150, 300), fill='blue', width=2)
draw.line((20, 30, 40, 50), fill='red', width=3)
draw.point(((30, 40), (10, 20), (14, 25), (35, 10), (14, 28), (17, 25)), fill="black")

colors = ['black', 'red', 'green', 'yellow',(90,90,20),(20,34,21),(123,245,32),(67,32,187)]  # for points color
fill_color = [(20, 10, 40), (90, 30, 20), (222, 43, 190), (40, 43, 123), (59, 23, 109),(10,38,198),(234,221,255)]  # for line color

def gen_captcha_img():
    str = generate_string()
    print(str)
    text_color = random.choice(colors)
    font_name = "D:/OneDrive/Desktop/Fullstack/Captcha_project/copyduck/Copyduck.ttf"
    font = ImageFont.truetype(font_name, 30)
    draw.text((50, 50), str, fill=text_color,font=font)  # Draw the generated string onto the image

    # draw some random lines
    for i in range(5,random.randrange(6, 10)):
        draw.line((get_location(), get_location()), fill=random.choice(fill_color), width=random.randrange(2,5))

    # draw some random points
    for i in range(10,random.randrange(11, 20)):
        draw.point((get_location(), get_location(), get_location(), get_location(), get_location(), get_location(), get_location(), get_location(), get_location(), get_location()), fill=random.choice(colors))


gen_captcha_img()  # Call the function to generate the captcha image
img.save(r'D:\OneDrive\Desktop\Fullstack\Captcha_project\blanc_img.png')
