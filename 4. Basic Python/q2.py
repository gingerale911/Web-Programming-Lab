def binary_search(arr, high, low, key):
    if low > high:
        return -1
    
    mid = (high+low)//2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, mid-1, low, key)
    else:
        return binary_search(arr, high, mid+1, key)
    
arr = list(map(int, input("Enter Sorted Elements: ").split()))
key = int(input("Eneter Key: "))
result = binary_search(arr, len(arr)-1, 0, key)

if result != -1:
    print("Element found at index", result,"Siuu")

else:
    print("Result Not Found")

