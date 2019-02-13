
import numpy as np

def crop(image, height, width):
    '''
    Function to crop images
    Parameters:
    image, a 3d array of the image (can be obtained using plt.imread(image))
    height, integer, the desired height of the cropped image
    width, integer, the desired width of the cropped image
    Returns:
    cropped_image, a 3d array with dimensions height x width x 3
    Example:
    crop(image, 10, 15) returns an array with shape (10, 15, 3)
    '''
    #---------------------------------------Exception Handling----------------------------------------------------#
    # Exception handling for input validation like Type error, invalid values , unrealistic desired dimension     #
    #-------------------------------------------------------------------------------------------------------------#
    myError = False
    if type(height) != int or type(width) !=int or type(image) is not np.ndarray:
        myError = TypeError('Invalid Type')
    elif height<0 or width <0 or height ==0 or width ==0 or height == int(-1e30) or width==int(-1e30):
        myError = ValueError('Desired dimension should be positive')
    elif height == image.shape[1] + 1 or width == image.shape[2] + 1:
        myError = ValueError('Desired dimension should be less than original dimension')             
    if myError:
        raise myError
    #----------------------------------------Initialisation-------------------------------------------------------#    
    height = image.shape[1]-height
    width  = image.shape[2]-width
    #----------------------------------------Main Processing------------------------------------------------------# 
    # Removing rows from top and bottom by checking if the desired height is even or odd. For even height         #
    # removing half number of rows of desired height from top and half number of rows of desired height from      #
    # bottom. For Odd , dividing the height - 1 value and removing half number of rows from top , half + 1 number #
    # row from bottom.Similar treatment for removing columns from left and right .                                #
    #-------------------------------------------------------------------------------------------------------------#
    if height % 2 ==0:                                     # For even desired height
        start_row = int(height/2)                          
        end_row   = int(image.shape[1]-height/2)          
    else:                                                  # For Odd desired height
        start_row = int((height-1)/2)
        end_row   = int((image.shape[1]-(height-1)/2)-1)  
        
    if width % 2 ==0:                                      # For even desired width
        start_col = int(width/2)
        end_col   = int((image.shape[2]-width/2))               
    else:                                                  # For Odd desired width
        start_col = int((width-1)/2)
        end_col   = int((image.shape[2]-(width-1)/2)-1)
                
    img = image[:,start_row:end_row,start_col:end_col]     # Cropping image from all sides.
    
    return(img)
