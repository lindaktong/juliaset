
# coding: utf-8

# In[134]:


#sources: 
    #Tariq Rashid, Make Your Own Mandelbrot
    #https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linspace.html
    #https://docs.scipy.org/doc/numpy-1.13.0/user/quickstart.html
    #https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
    #https://stackoverflow.com/questions/42644158/matplotlib-not-displaying-image
    #https://docs.python.org/2/library/cmath.html


# In[136]:


2*3


# In[138]:


print("Hello World!")


# In[139]:


#assign the complex number (2+3i) to c


# In[140]:


c = complex(2,3)
print(c)


# In[141]:


#print c multiplied by (1-4i)
print(c*complex(1,-4))


# In[142]:


#print c squared
print(c*c)


# In[143]:


#import numpy in Python shell
import numpy as np


# In[144]:


#generates equally spaced vectors
#creates a series of numbers from a starting value, up to an upper value, spaced regularly apart.
np.linspace(0.0, 5.0, 5)


# In[145]:


#linspace found 5 evenly spaced points between 0 and 5


# In[146]:


#create a rectangle with bottom left at (-2,-2) and the top right at (4,2)
#horizontal length of 6, vertical length of 4
#divide the horizontal length into 12 sections and the vertical into 8

#horizontal side from -2 to 4

import numpy as np
np.linspace(-2.0,4.0,13)


# In[147]:


#vertical side from -2 to 2
np.linspace(-2.0, 2.0, 9)


# In[148]:


#define list of all points in the rectangle of interest
x_list = np.linspace(-2.0,4.0,13)
y_list = np.linspace(-2.0, 2.0, 9)


# In[149]:


#print list of all points
#for each value in the x_list go through the y_list, and for each of combination print out the values.
for x in x_list:
    for y in y_list:
        print (x,y)
        pass
    pass


# In[150]:


#this is the list of all the points we want to test inside a rectangular section


# In[2]:


#mandelbrot function, takes the fixed paramter and maxiter, the maximum number of iterations matter, as inputs
#mandelbrot set is the set of complex numbers for which the iterated function does not diverge

def julia(z,c,maxiter):
    
    #start iterating and stop when it's maxiter times
    for iteration in range(maxiter):
        
        #the main function which generates the output value of z from the input values using the formula (z^2) + c
        z = (z*z) + c
        
        #check if the Pythagorean magnitude (or absolute value) of the output complex number z is bigger than 4
        #if so, stop iterating as divergence has occured already
        if abs(z)>4:
            break #exits out of loop
            pass #null statement/acts as placehoder
        pass
    
    #return the number of iterations we actually did, not the final value of z
    #this tells us how quickly the values diverged past the magnitude threshold of 4
    return iteration

import numpy as np

#set the location and size of the complex plane rectangle 
xvalues = np.linspace(-2, 2, 1000) #creates a list of 1000 points evenly placed between -2 and 2
yvalues = np.linspace(-2, 2, 1000)  #creates a list of 1000 points evenly placed between -2 and 2

#size of these lists of x and y values 

xlen = len(xvalues)
#assigns length of of the list and assigns it to variable xlen
#since xvalues contains 1000 points, we know len(xvalues) is 1000
#good practice to create changeable parameters

ylen = len(yvalues)
#assigns length of of the list and assigns it to variable ylen

#value of c is unique for each Julia set
c = complex(-0.35,0.65)

#create array of color values with size xlen by ylen
atlas = np.empty ((xlen, ylen))

#fill array with color values based on # of iterations

for ix in range(xlen):
    for iy in range(ylen):
    #nested for loop
    #loops count through rows and columns of atlas using the variables ix and iy
        
        #this is how we construct the complex number c
        zx = xvalues[ix]
        zy = yvalues[iy]
        z = complex(zx,zy)
        
        atlas[ix,iy]= julia(z,c,80) #updates contents of array with returned value from mandel function
        
        pass
    pass

get_ipython().magic('matplotlib inline')
#enable automatic visualization of your plots when the cell has finished executing
from matplotlib import pyplot as plt

#set the figure size
plt.figure(figsize=(18,18))

#plot the array atlas as an image
plt.imshow(atlas.T, interpolation="nearest", cmap="jet")


# In[4]:


#zoom in by changing bottom left and top right points

def julia(z,c,maxiter):
    for iteration in range(maxiter):
        z = (z*z) + c
        if abs(z)>4:
            break #exits out of loop
            pass #null statement/acts as placehoder
        pass
    return iteration

import numpy as np
xvalues = np.linspace(-0.5, 1, 2000) #creates a list of 1000 points evenly placed between -2 and 2
yvalues = np.linspace(-1, 0.5, 2000)  #creates a list of 1000 points evenly placed between -2 and 2
xlen = len(xvalues)
ylen = len(yvalues)
c = complex(-0.35,0.65)
atlas = np.empty ((xlen, ylen))
for ix in range(xlen):
    for iy in range(ylen):
        zx = xvalues[ix]
        zy = yvalues[iy]
        z = complex(zx,zy)
        atlas[ix,iy]= julia(z,c,80) #updates contents of array with returned value from mandel function
        
        pass
    pass
get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
plt.figure(figsize=(36,36))
plt.imshow(atlas.T, interpolation="nearest", cmap="jet")


# In[154]:


#create a more detailed image by setting a higher value for maximum iterations

def mandel(c,maxiter):
    z=complex(0,0)
    for iteration in range(maxiter):
        z = (z*z) + c
        if abs(z)>4:
            break 
            pass 
        pass
    return iteration

import numpy as np

#set the location and size of the atlas rectangle
xvalues = np.linspace(-0.22, -0.21, 1000)
yvalues = np.linspace(-0.70, -0.69, 1000)
xlen = len(xvalues)
ylen = len(yvalues)

atlas = np.empty ((xlen, ylen))

for ix in range(xlen):
    for iy in range(ylen):
        cx = xvalues[ix]
        cy = yvalues[iy]
        c = complex(cx,cy)  
        atlas[ix,iy]= mandel(c,120) #increase maxiter
        pass
    pass

get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
plt.figure(figsize=(18,18))
plt.imshow(atlas.T, interpolation="nearest", cmap="jet")


# In[6]:


#change colors?

def mandel(c,maxiter):
    z=complex(0,0)
    for iteration in range(maxiter):
        z = (z*z) + c
        if abs(z)>4:
            break 
            pass 
        pass
    return iteration

import numpy as np

xvalues = np.linspace(-2.25, 0.75, 1000)
yvalues = np.linspace(-1.5, 1.5, 1000)
xlen = len(xvalues)
ylen = len(yvalues)

atlas = np.empty ((xlen, ylen))

for ix in range(xlen):
    for iy in range(ylen):
        cx = xvalues[ix]
        cy = yvalues[iy]
        c = complex(cx,cy)  
        atlas[ix,iy]= mandel(c,250)
        pass
    pass

get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
plt.figure(figsize=(18,18))
plt.imshow(atlas.T, interpolation="nearest", cmap="jet")

# set the figure size
figsize(18,18)

# create a smoothed image of the original by applying a Gaussian blur filter
smoothed_atlas = scipy.ndimage.gaussian_filter(atlas.T, 1)

# plot the array atlas as an image, with its values represented as colours, peculiarity of python that we have to transpose the array
imshow(smoothed_atlas, interpolation="nearest", cmap="jet")


# In[7]:


#Gaussian blur filter

def mandel(c,maxiter):
    z=complex(0,0)
    for iteration in range(maxiter):
        z = (z*z) + c
        if abs(z)>4:
            break 
            pass 
        pass
    return iteration

import numpy as np

xvalues = np.linspace(-2.25, 0.75, 1000)
yvalues = np.linspace(-1.5, 1.5, 1000)
xlen = len(xvalues)
ylen = len(yvalues)

atlas = np.empty ((xlen, ylen))

for ix in range(xlen):
    for iy in range(ylen):
        cx = xvalues[ix]
        cy = yvalues[iy]
        c = complex(cx,cy)  
        atlas[ix,iy]= mandel(c,250)
        pass
    pass

get_ipython().magic('matplotlib inline')
from matplotlib import pyplot as plt
plt.figure(figsize=(18,18))
plt.imshow(atlas.T, interpolation="nearest", cmap="jet")

#sobel
sx = scipy.ndimage.sobel(atlas, axis=0, mode='constant')
sy = scipy.ndimage.sobel(atlas, axis=1, mode='constant')
sob = hypot(sx, sy)

#set the figure size
figsize(18,18)
imshow(sob.T, interpolation="nearest", cmap="jet")


# In[5]:


# set the figure size
figsize(18,18)

# create a smoothed image of the original by applying a Gaussian blur filter
smoothed_atlas = scipy.ndimage.gaussian_filter(atlas.T, 1)

# plot the array atlas as an image, with its values represented as colours, peculiarity of python that we have to transpose the array
imshow(smoothed_atlas, interpolation="nearest", cmap="jet")


# In[1]:


# python 3 version of code for making your own julia fractal
# 
# blog and book at http://makeyourownmandelbrot.blogspot.co.uk
get_ipython().magic('pylab inline')
# image processing library
import scipy.ndimage
# set the location and size of the atlas rectangle
xvalues = linspace(-2, 2, 1000)
yvalues = linspace(-2, 2, 1000)

# size of these lists of x and y values
xlen = len(xvalues)
ylen = len(yvalues)

# value of c (unique for each Julia set)
c = complex(-0.166517,-0.662029)

# julia function, takes the fixed parameters z and c, and the maximum number of iterations maxiter, as inputs
def julia(z, c, maxiter):
    
    # start iterating and stop when it's done maxiter times
    for iteration in range(maxiter):
        
        # the main function which generates the output value of z from the input values using the formula (z^2) + c
        z = (z*z) + c
        
        # check if the (pythagorean) magnitude of the output complex number z is bigger than 4, and if so stop iterating as we've diverged already
        if abs(z) > 4:
            break
            pass
        pass
    
    # return the number of iterations we actually did, not the final value of z, as this tells us how quickly the values diverged past the magnitude threshold of 4
    return iteration

# create an array of the right size to represent the atlas, we use the number of items in xvalues and yvalues
atlas = empty((xlen,ylen))

# go through each point in this atlas array and test to see how many iterations are needed to diverge (or reach the maximum iterations when not diverging)
for ix in range(xlen):
    for iy in range(ylen):
        
        # at this point in the array, work out what the actual real and imaginary parts of x are by looking it up in the xvalue and yvalue lists
        zx = xvalues[ix]
        zy = yvalues[iy]
        z = complex(zx, zy)
        
        # now we know what c is for this place in the atlas, apply the julia() function to return the number of iterations it took to diverge
        # we use 80 maximum iterations to stop and accept the function didn't diverge
        atlas[ix,iy] = julia(z, c, 80)
        
        pass
    pass

# set the figure size
figsize(18,18)

# plot the array atlas as an image, with its values represented as colours, peculiarity of python that we have to transpose the array
imshow(atlas.T, interpolation="nearest", cmap="jet")


# In[2]:


# set the figure size
figsize(18,18)

# create a smoothed image of the original by applying a Gaussian blur filter
#this calculates a new image array, based on the original one
#however, each new value is smoothed based on its neighbours values.

smoothed_atlas = scipy.ndimage.gaussian_filter(atlas.T, 2)

# plot the array atlas as an image, with its values represented as colours, peculiarity of python that we have to transpose the array
imshow(smoothed_atlas, interpolation="nearest", cmap="jet")


# In[3]:


# sobel
sx = scipy.ndimage.sobel(atlas, axis=0, mode='constant')
sy = scipy.ndimage.sobel(atlas, axis=1, mode='constant')
sob = hypot(sx, sy)


figsize(18,18)
imshow(sob.T, interpolation="nearest", cmap="jet")

