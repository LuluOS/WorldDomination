from PIL import Image, ImageFont, ImageDraw
import easygui, sys


#""" Quicksort """
#""" http://hetland.org/coding/python/quicksort.html """
def partition(list, start, end):
  pivot = list[end] # Partition around the last value
  bottom = start-1  # Start outside the area to be partitioned
  top = end

  done = 0
  while not done: # Until all elements are partitioned...
    while not done: # Until we find an out of place element...
      bottom = bottom+1 # ... move the bottom up.

      if bottom == top: # If we hit the top...
        done = 1  # ... we are done.
        break

      if list[bottom] > pivot:  # Is the bottom out of place?
        list[top] = list[bottom]  # Then put it at the top...
        break                      # ... and start searching from the top.

    while not done: # Until we find an out of place element...
      top = top-1   # ... move the top down.

      if top == bottom: # If we hit the bottom...
        done = 1    # ... we are done.
        break

      if list[top] < pivot: # Is the top out of place?
        list[bottom] = list[top]  # Then put it at the bottom...
        break # ...and start searching from the bottom.

  list[top] = pivot # Put the pivot in its place.
  return top  # Return the split point

def quicksort(list, start, end):
  if (start < end):                            # If there are two or more elements...
    split = partition(list, start, end)    # ... partition the sublist...
    quicksort(list, start, split-1)        # ... and sort both halves.
    quicksort(list, split+1, end)
  else:
    return

#""" GroupPixel is a function that pick a group of 8x8 pixel and return the average   """
def GroupPixel(im, xstart, ystart, px):
    aveap = 0
    for y in range (ystart, ystart+px, 1):
        for x in range (xstart, xstart+px, 1):
            a = im.getpixel((x,y))
            #print ("A: %d" %(a))
            aveap = aveap + a
    return (aveap / (px*px))

#""" FuncColor is a function that pick a group of 8x8 pixel and return the colors   """
def FuncColor(im, xstart, ystart, px):
    red = []
    green = []
    blue = []
    for y in range (ystart, ystart+px):
        for x in range (xstart, xstart+px):
            r,g,b = im.getpixel((x,y))
            red.append(r)
            green.append(g)
            blue.append(b)
    sizeArray = (px*px)-1
    quicksort(red,0,sizeArray)
    quicksort(green,0,sizeArray)
    quicksort(blue,0,sizeArray)

    media = round((px*px)/2)

    return (red[media],green[media],blue[media])

#""" Function that manipulates the progress bar """
def ProgressBar(progress):
    barLength = 50 # Modify this to change the length of the progress bar
    status = ""
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1:.2f} % {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()
    #print(text, end="\r")

#""" OpenImage is a function open PNG and return the image """
def OpenImage(name):
    im = Image.open(name).convert('RGB') #""" converting to RGB """
    imbnw = Image.open(name).convert('L')  #""" converting to B&W """
    #imbnw.save(name + 'BnW.png') #""" save as  """
    return im, imbnw

#""" KnowFormatImage is a function that discovers what is the image format """
def KnowFormatImage(name):
    imageFormat = ""
    for i in range (len(name)-3,len(name)):
        #print(name[i])
        imageFormat += name[i]
    return imageFormat

#""" NewNameImage is a function that manipulates the role string and pick just the name of the image """
def NewNameImage(name):
    newName = ""
    count = len(name)-1
    flag = True

    while (flag):
        if (name[count] == '\\'):
            flag = False
        else:
            count = count - 1

    for i in range (count+1,len(name)-4):
        newName += name[i]

    return newName

#""" These function return a list of divisors """
def getDivisors(img):
    x = img.size[0]
    y = img.size[1]

    xArray = []
    yArray = []
    matching = []
    for i in range ( 1, round(x/8)):
        if x % i == 0:
            xArray.append(i)

    for j in range ( 1, round(y/8)):
        if y % j == 0:
            yArray.append(j)

    matching = list(set(xArray) & set(yArray))

    length = len(matching)
    quicksort(matching,0,length - 1)

    return matching

########################################################################################################################
#""" Main """

name = easygui.fileopenbox() #""" ask to the user the name of the image """
imageType = KnowFormatImage(name)
newName = NewNameImage(name)
img, imbnw = OpenImage(name)

msg = "Choose a density?"
title = "Density/Font Sizing"
matching = getDivisors(img)
length = len(matching)

#""" The choices is going to be based on the size of the list from
#  the divisors if the number repeats it is going to show just one time """
choices = [matching[1], matching[round(length/8)], matching[round(length/6)], matching[round(length/4)], matching[round(length/2)]]

#""" there is no way to specify a custom order. The reason is that the data must be sorted in order
#   for the "jump to" feature (namely, to jump down in the list by pressing keyboard keys) to work.
#   https://media.readthedocs.org/pdf/easygui/master/easygui.pdf """

choice = easygui.choicebox(msg, title, choices)
size = int(choice)

newImage = Image.new(img.mode, img.size, "white") #""" creating a new image """
draw = ImageDraw.Draw(newImage) #""" allowing a draw in the new image """

#size = int(input("Enter the size of the group of pixel: ")) #""" size of group of pixel """
fontSize = round((10*size)/8) #""" font size is based on the size of the group of pixel """
font = ImageFont.truetype("Aller_Rg.ttf",fontSize) #""" defining the font and its size (size to a pixel 8) """

#""" our chars darker to lighter """
greyscale=['@', '%', '#', '$', '&', 'e' ,'+', '~', ',', '.', ' ']

#""" Divide the big image in small squares that has the size 8x8 """
lines = img.size[0]/size #""" Number of lines in the image (X-Axes) """
columns = img.size[1]/size  #""" Number of columns in the image (Y-Axes) """
squares = (lines * columns)  #""" Amount of small squares with the size 8x8 """
count = 0

# """ Y-axes incremented by 8 """
for j in range(0, img.size[1], size):
    # """ X-axes incremented by 8 """
    for i in range (0, img.size[0], size):
        a,b,c = FuncColor(img, i, j, size)
        p = GroupPixel(imbnw, i, j, size)
        scale = p / 25.5 #""" our scale to change the group of the pixel into one char """
        scale = round(scale)
        draw.text((i,j),greyscale[scale], font=font, fill=(a,b,c))

        #""" Manipulating the percentage of the progress bar
        #    squares -> 100% = 1
        #    count   -> x% = x
        # So squares * x = count * 1
        #    x =  count/squares """
        count = count + 1
        x = count/squares
        ProgressBar(x)

newImage.save(newName + '_' + str(size) + '_' + 'Char.' + imageType) #""" save the new image """
newImage.show() #""" showing the new image """

exit()