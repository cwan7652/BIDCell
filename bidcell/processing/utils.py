import numpy as np

def get_patches_coords(size, size_patch):
    """ Get start and end locations of patches in a large image given the image patch sizes """

    if size <= size_patch:
        max_size = size
        coords = [(0, max_size)]
    else:
        max_size = size_patch
        starts = list(np.arange(0, size, size_patch))
        ends = [x+size_patch if x+size_patch <= size else size for x in starts]
        coords = list(zip(starts, ends))
    
    return coords, max_size
    
