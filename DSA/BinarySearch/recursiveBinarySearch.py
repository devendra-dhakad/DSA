def recursiveBinarySearch(arr, z):
    print(arr )
    if (len(arr) == 0):
        return False
    else:
        mid = len(arr)//2
        print(mid)
        if (arr[mid] == z):
            return True
        else:
            if(arr[mid] < z):
                return recursiveBinarySearch(arr[mid+1:], z)
            else:
                return recursiveBinarySearch(arr[:mid], z)
    

arr = [11,22,33,44,55,66,77,88,99]

print(recursiveBinarySearch(arr, 22))
