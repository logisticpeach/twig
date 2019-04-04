def splitArray(array, slices):
    if array == None:
        raise ValueError

    if slices <= 0:
        raise ValueError

    arrayLength = len(array)

    if arrayLength == 0:
        return []

    if slices > arrayLength:
        raise ValueError

    # Use workingLength when calculating the optimum
    # bucket size
    workingLength = arrayLength

    remainder = arrayLength % slices

    # Find the correct bucket size if things don't divide nicely 
    if remainder > 0:
       workingLength = workingLength + remainder

    bucketSize = workingLength // slices

    if bucketSize > arrayLength:
        return [array]

    leftoverElements = arrayLength % bucketSize

    results = []

    for i in range (0, slices):
        if i == slices-1 and leftoverElements > 0:
            results.append(array[arrayLength-leftoverElements:])
        else:
            start = i*bucketSize
            end = start + bucketSize
            results.append(array[start:end])

    return results

   
