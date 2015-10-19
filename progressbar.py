import time, sys

###http://stackoverflow.com/questions/3160699/python-progress-bar

# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""

    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


# update_progress test script
print ("")
print ("progress : 0->1")
for i in range(101):
    time.sleep(0.1)
    update_progress(i/100.0)

print ("")
print ("Test completed")
time.sleep(10)