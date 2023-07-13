
#Write a recursive binary search algorithm that searches for a target element within a sorted array. The algorithm follows these steps:
# Define a recursive function binary_search_recursive(array, target, low, high)
# If low is greater than high, return -1 to indicate that the target was not found.
# Calculate the middle index of the current range as mid = (low + high) // 2.
# If array[mid] is equal to the target, return mid to indicate that the target was found at the current index.
# If array[mid] is greater than the target, recursively call binary_search_recursive(array, target, low, mid - 1) to search in the left half of the array.
# If array[mid] is less than the target, recursively call binary_search_recursive(array, target, mid + 1, high) to search in the right half of the array.


def binary_search_recursive(array, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
       return binary_search_recursive(array, target, low, mid - 1)
    else:   
        return binary_search_recursive(array, target, mid + 1, high)
print(binary_search_recursive([5,6,7,8],7,0,len([5,6,7,8])-1))
