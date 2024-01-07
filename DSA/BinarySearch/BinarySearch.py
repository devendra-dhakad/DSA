def BinarySearch(arr, z):
    first = 0
    last = len(arr)-1
    while(first <= last):
        mid = (first+last)//2
        if (arr[mid] == z):
            return mid
        elif (mid < z):
            first =  mid + 1
        else:
            last = mid - 1
    return None
            
    

arr = [11,22,33,44,55,66,77,88,99]

print(BinarySearch(arr, 77))
