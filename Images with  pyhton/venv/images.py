from PIL import  Image, ImageFilter
img =Image.open('./pokidesk/astro.jpg')
# img_filter = img.convert("L")
# img_filter.save("grey.png",'png')
# rotate = img.rotate(180)
# rotate.save("grey.png",'png')
# resize = img.resize(((180,180)))
# resize.save("grey.png","png")

# img_filter.show()
# print(dir(img))
# box = (100, 100, 400, 400)
# region = img.crop(box)
# region.save("ssa.png","png")

# it will resize the image and
# name it thumbnail.jpg
# new_img = img.resize((400,400))
# new_img.save('thumbnail.jpg')py

#  'thumbnil' will compressed the img inteligently.
# in here size s (400,381)
# it will use for making profile picture.
img.thumbnail((400,400))
img.save("thumbnail.jpg")
print(img.size)