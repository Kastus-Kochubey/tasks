from PIL import Image
from random import randint, random

# x = 50

# def image_convert(inp_name, filter, outp_name):
# filters = {negative : '',}
img = Image.open('image2.jpg')
pix = img.load()
width, height = img.size
q1, q2, q3 = random(), random(), random()
for i in range(height):
    # print(f'{i * 100 // height}%', end='\r')
    print(i)
    for j in range(width):
        r, g, b = pix[j, i]
        # pix[j,i] = tuple (map(lambda x: 255-x,(r, g, b)))
        # 1 n = (r+g+b)//3
        # 1 n = 255 if n > 110 else 0
        # 1 pix[j,i] = n,n,n
        # 2 pix[j, i] = randint(r-x,r+x)%256,randint(g-x,g+x)%256, randint(b-x,b+x)%256

        # if r < 130 or g > 130 or b > 130:
        pix[j, i] = max(int(r * q1) % 256, randint(0, r)), max(int(g * q2) % 256, randint(0, g)), max(int(b * q3) % 256, randint(0, b))
        # pix[j, i] = r ** 3 % 256, b ** 3 % 256, b ** 3 % 256
        # pix[j, i] = r * randint(2, 15) % 256, b * 7 % 256, b * 5 % 256
        # if (r + g + b) // 3 < 130:
            # pix[j, i] = r * randint(0, 256) % 256, g * randint(0, 256) % 256, b * randint(0, 256) % 256
            # pix[j, i] = int(r * random()) % 256, int(g * random()) % 256, int(b * random()) % 256
        # else:
        #     # pix[j, i] = randint(120, 165), randint(20, 60), 50
        #     pix[j, i] = r ** 3 % 256, b ** 3 % 256, b ** 3 % 256

# img.transpose(Image.ROTATE_90).save('image.jpg')
img.save('image5.jpg')
