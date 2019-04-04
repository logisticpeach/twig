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

    workingLength = arrayLength

    leftoverElements = arrayLength % slices

    if leftoverElements > 0:
       workingLength = workingLength + leftoverElements

    bucketSize = workingLength // slices

    if bucketSize > arrayLength:
        return [array]

    remainder = arrayLength % bucketSize

    results = []

    for i in range (0, slices):

        if i == slices-1 and remainder > 0:
            results.append(array[arrayLength-remainder:])
        else:
            start = i*bucketSize
            end = start + bucketSize
            results.append(array[start:end])

    return results

   