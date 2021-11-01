def binarySearch(arr,value, lower_key, upper_key):
    start=0
    end=len(arr)-1
    while end>=start:
        middle=(end+start)//2
        if(value>=arr[middle][lower_key] and value<=arr[middle][upper_key]):
            return middle
        elif(value>arr[middle][upper_key]):
            start=middle+1
        else:
            end=middle-1
    return -1;