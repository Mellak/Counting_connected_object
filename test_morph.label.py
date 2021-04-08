'''
Quick tuto to understand skimage.morphology.label
'''

import numpy as np
from skimage import morphology as morph
import pylab as plt



#Part I : Discovering
'''
Here we will generate an image of 9x9 pixels, with diagonal pixels == 1
'''

x = np.eye(9).astype(int)


'''
Here we will change value of some pixels to 1
'''
x[3][2] = 1
x[7][5] = 1
x[8][2] = 1
x[4][7] = 1
x[1][3] = 1

'''
Definition : Two pixels are connected when they are neighbors and have the same value.
In 2D, they can be neighbors either in a 1- or 2-connected sense.


With :  
        1-connectivity      2-connectivity     
           [ ]           [ ]  [ ]  [ ]         
            |               \  |  /            
      [ ]--[x]--[ ]      [ ]--[x]--[ ]    
            |               /  |  \         
           [ ]           [ ]  [ ]  [ ]


Ref : https://github.com/scikit-image/scikit-image/blob/v0.14.3/skimage/measure/_label.py#L4 Line:8 :P
'''

'''
1-connectivity
'''
blobs_1 = morph.label(x == 1, connectivity=1)


'''
2-connectivity 
'''
blobs_2 = morph.label(x == 1, connectivity=2)


'''
In results each region of pixels have a different label.
'''
f = plt.figure()
f.add_subplot(1, 2, 1)
plt.imshow(x)
f.add_subplot(1, 2, 1)
plt.imshow(blobs_1)
f.add_subplot(1, 2, 2)
plt.imshow(blobs_2)

plt.show(block=True)



'''
********************************************************************************************************************'
'''

#Part II : Counting number of objects in an image :
import random
from random import seed

'''
Generate a black image with 50x50 pixels
'''

clusterMask = np.zeros((50, 50))
'''loop to generate (5) objects'''
for i in range(5) :

    '''Here we will generate random center for our rectangles...'''
    seed()
    clusterH = random.randint(5, 45)
    seed()
    clusterW = random.randint(5, 45)

    '''The width and height of our rectangle will be S*2'''
    S = 2

    '''Color pixels with 1'''
    clusterMask[clusterH - 2 * S: clusterH + 2 * S, clusterW - 2 * S: clusterW + 2 * S] = 1

'''Display'''
plt.imshow(clusterMask)
plt.show()


'''Labeling objects with connectivity 1'''
blobs_1 = morph.label(clusterMask == 1, connectivity=1)


'''Labeling objects with connectivity 2'''
blobs_2 = morph.label(clusterMask == 1, connectivity=2)


print('with connectivity 2 there is {} object, and with connectivity 1 we have {} object.'.format(blobs_2.max(),blobs_1.max()))
