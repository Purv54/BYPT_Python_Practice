from PIL import Image

mac = Image.open("mac.jpeg")
# mac.show()
# The PIL (Pillow) library is used for opening, manipulating, and saving many different image file formats. 
# The Image class is used to represent an image. 
# The open() function is used to open an image file and create an Image object. 
# The show() method is used to display the image.   
# mac.crop((0, 0, 400, 400)).show()
# The crop() method is used to crop the image. 
# The argument is a tuple that defines the left, upper, right, and lower pixel coordinates of the box to be cropped. 
# The method returns a new Image object that is the cropped image. 
# The show() method is then used to display the cropped image.

# print(mac.size)

# x = 0
# y = 0 
# w = 234 / 2
# h = 215
# mac.crop((x,y,w,h)).show()
# The size attribute of the Image object returns a tuple containing the width and height of the image in pixels. 
# In this code, we are cropping the image using the crop() method. 
# The crop() method takes a tuple of four values that represent the left, upper, right, and lower pixel coordinates of the box to be cropped. 
# In this case, we are  cropping the image from the top-left corner (0, 0) to the point (w, h), where w is half of the width of the image and h is the full height of the image.
# mac.rotate(90).show()
