def intersection(l1, l2):
    function = list(filter(lambda x: x in l1, l2))
    return function


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

intersection_result = intersection(list1, list2)

print(intersection_result)