def binary_search(my_array, target, low, high):
    # Set the mid point
    mid = (low + high) // 2

    Base case: if not found, exit
    if low > high:
        return False

    # Check mid point of array
    if my_array[mid] != target:
        # Case 1: target is less than mid point, move high to mid - 1
        if target < my_array[mid]:
            return binary_search(my_array, target, low, mid - 1)

        # Case 2: target is more than mid point, move low to mid + 1
        if target > my_array[mid]:
            return binary_search(my_array, target, mid + 1, high)

    # Base case: if found, exit, return index
    else:
        return mid


my_list = list(range(1, 201))
print(binary_search(my_list, , 0, len(my_list)-1))
