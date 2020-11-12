from PIL import Image

img = Image.open('defaultImage.png')

img = img.resize((300, 200))

img.save('defaultImage.png')

