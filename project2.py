from PIL import Image

def GroupPixel(im, xstart, ystart):
    aveap = 0
    for y in range (ystart, ystart+8, 1):
        for x in range (xstart, xstart+8, 1):
            a, b = im.getpixel((x,y))
            #print (a, b)
            aveap = aveap + a
    return (aveap / 100)

im = Image.open('project2.png').convert('LA')
#print(im.format, im.size, im.mode)
#im.show()

for j in range(0, im.size[1], 8):
    for i in range (0, im.size[0], 8):
        p = GroupPixel(im, i, j)
        #print("x = %d y = %d" %(i,j))
        print ("P = %.2f" %(p))
        scale = p / 25.5
        print ("Scale = %.2f" %(scale))
        print ("ROUND = %d" %(round(scale)))