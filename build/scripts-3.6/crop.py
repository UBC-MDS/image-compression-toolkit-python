
import numpy as np
import os
from skimage.io import imread, imsave

def crop(img_path, H, W, out_path):
    """
    Function to crop and save an image.

    Parameters:
    ----------
    img_path - String , file path of the image .
    H        - Integer, the desired height of the cropped image
    W        - Integer, the desired width of the cropped image

    out_path - String, file path to the cropped image
    
    Returns:
    -------
    String, file path to the cropped image (same as out_path)
    

    Example:
    -------
    crop("data/sample.png", 10, 15)
    saves the image and returns the path of the cropped image.
    """
    #---------------------------------------Exception Handling----------------------------------------------------#
    # Exception handling for input validation like Type error, invalid values , unrealistic desired dimension     #
    #-------------------------------------------------------------------------------------------------------------#
    if type(img_path) != str or type(out_path) != str:
        raise TypeError("Image path not correct, make sure you are passing a string!")
    if type(H) != int or type(W) !=int:
        raise TypeError('Invalid Type')
    elif H<0 or W <0 or H ==0 or W ==0:
        raise ValueError('Desired dimension should be positive')
    elif H >= imread(img_path).shape[0] + 1 or W >= imread(img_path).shape[1] + 1:
        raise ValueError('Desired dimension should be less than original dimension')
    #----------------------------------------Initialisation-------------------------------------------------------#
    image  = imread(img_path)
    height = image.shape[0]-H
    width  = image.shape[1]-W
    #----------------------------------------Main Processing------------------------------------------------------#
    # Removing rows from top and bottom by checking if the desired height is even or odd. For even height         #
    # removing half number of rows of desired height from top and half number of rows of desired height from      #
    # bottom. For Odd , dividing the height - 1 value and removing half number of rows from top , half + 1 number #
    # row from bottom.Similar treatment for removing columns from left and right .                                #
    #-------------------------------------------------------------------------------------------------------------#
    if height % 2 ==0:                                     # For even desired height
        start_row = int(height/2)
        end_row   = int(image.shape[0]-height/2)
    else:                                                  # For Odd desired height
        start_row = int((height-1)/2)
        end_row   = int((image.shape[0]-(height-1)/2)-1)

    if width % 2 ==0:                                      # For even desired width
        start_col = int(width/2)
        end_col   = int((image.shape[1]-width/2))
    else:                                                  # For Odd desired width
        start_col = int((width-1)/2)
        end_col   = int((image.shape[1]-(width-1)/2)-1)

    img = image[start_row:end_row,start_col:end_col,:]     # Cropping image from all sides.
    #-----------------------------------------Saving Cropped Image-----------------------------------------------#
    # Saving the image                                                         #
    #------------------------------------------------------------------------------------------------------------#

    imsave(out_path, img)

    return out_path

