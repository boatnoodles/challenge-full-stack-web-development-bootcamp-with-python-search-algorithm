# Look for all the matches, vs normal linear search which only returns the first instance of the target


def global_linear_search(target, my_list):
    result = []
    for i in range(len(my_list)):
        if target == my_list[i]:
            result.append(i)
    return result


bananas_arr = list("bananas")
print(global_linear_search("a", bananas_arr))
