import rand

def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = []

    # Merge elements from both arrays in sorted order
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1

    # Append the remaining elements from both arrays
    mergeArr.extend(leftArr[leftIndex:])
    mergeArr.extend(rightArr[rightIndex:])
    
    return mergeArr
arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)


