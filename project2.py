from PIL import Image, ImageFont, ImageDraw

#""" GroupPixel is a function that pick a group of 8x8 pixel and return the average   """
def GroupPixel(im, xstart, ystart, px):
    aveap = 0
    for y in range (ystart, ystart+px, 1):
        for x in range (xstart, xstart+px, 1):
            a = im.getpixel((x,y))
            #print ("A: %d" %(a))
            aveap = aveap + a
    return (aveap / (px*px))

#""" OpenImage is a function open PNG and return the image """
def OpenImage(name):
    im = Image.open(name + '.png').convert('L') #""" converting to B&W """
    im.save(name + 'BnW.png') #""" save as  """
    return im


#""" Main """
name = input("Name of the image: ") #""" ask to the user the name of the image """
img = OpenImage(name)

#print(im.format, im.size, im.mode)
#im.show()

newImage = Image.new(img.mode, img.size, "white") #""" creating a new image """

size = 8 #""" size of group of pixel """

draw = ImageDraw.Draw(newImage) #""" allowing a draw in the new image """
font = ImageFont.truetype("arial.ttf",8) #""" defining the font and its size (size to a pixel 8) """

#greyscale=['#', '@', '8', 'k', 'j', ';', ':', ',', '.', ' ', ' '] #""" our chars darker to lighter """
greyscale=['@', '%', '#', '$', '&', '|' ,';', ':', ',', '.', ' '] #""" our chars darker to lighter """

for j in range(0, img.size[1], size):
    for i in range (0, img.size[0], size):
        p = GroupPixel(img, i, j, size)
        #print("x = %d y = %d" %(i,j))
        #print ("P = %.2f" %(p))
        scale = p / 25.5 #""" our scale to change the group of the pixel into one char """
        #print ("Scale = %.2f" %(scale))
        #print ("ROUND = %d" %(round(scale)))
        scale = round(scale)
        draw.text((i,j),greyscale[scale], font=font)

newImage.show() #""" showing the new image """
newImage.save(name + 'Char.png') #""" save the new image """