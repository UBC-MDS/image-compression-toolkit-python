def compress(image, b):
    '''
    Function to compress images

    Parameters:
    image, a 3d array representation of the image
        like the one returned by plt.imread(image)
    
    b, the number of bits used in each entry in the array
        integer from 1 to 8
            1 = maximum compression
            8 = no compression

    Returns:
    compressed_image, an image with the same size as image but
        with fewer bits used to represent each entry

    Example:
    compress(image, 5)
    '''
    pass