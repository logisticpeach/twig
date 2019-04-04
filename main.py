def splitArray(array, slices):
    if array == None:
        raise ValueError

    if slices <= 0:
        raise ValueError
        
    return []