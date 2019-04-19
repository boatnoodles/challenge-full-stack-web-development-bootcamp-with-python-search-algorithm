def linear_search(target, my_list):
    # for index, num in enumerate(my_lsit):
    for i in range(len(my_list)):
        # if num == target:
        if target == my_list[i]:
            # return index
            return i
    else:
        return "not found"


random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]

# 2 (it returns the position of the number)
print(linear_search(18, random_numbers))
print(linear_search(9, random_numbers))
# not found
