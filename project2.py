from PIL import Image

#""" GroupPixel is a function that pick a group of 8x8 pixel and return the average   """
def GroupPixel(im, xstart, ystart, px):
    aveap = 0
    for y in range (ystart, ystart+px, 1):
        for x in range (xstart, xstart+px, 1):
            a = im.getpixel((x,y))
            print ("A: %d" %a)
            aveap = aveap + a
    return (aveap / 100)

im = Image.open('figure2.png').convert('L')
#print(im.format, im.size, im.mode)
#im.show()

size = 8
for j in range(0, im.size[1], size):
    for i in range (0, im.size[0], size):
        p = GroupPixel(im, i, j, size)
        #print("x = %d y = %d" %(i,j))
        print ("P = %.2f" %(p))
        scale = p / 25.5 #""" our scale to change the group of the pixel into one char """
        print ("Scale = %.2f" %(scale))
        print ("ROUND = %d" %(round(scale)))