def binary_search(target, my_list):
    # Start at mid point
    low = 0
    high = len(my_list) - 1

    while True:
        # Number is not found in the list
        if low > high:
            return False

        # Obtain the mid-point
        middle = (low + high) // 2

        # If midpoint/reference point is less than the target, move to the left
        if my_list[middle] < target:
            low = middle + 1
        # If midpoint/reference point is more than the target, move to the right
        elif my_list[middle] > target:
            high = middle - 1
        # Else it's been found
        else:
            return middle


print(binary_search(56, list(range(1, 201))))
