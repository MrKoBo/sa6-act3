numbers = [2,5,2,4, 7, 3]

bigger_num = lambda x, y: x if x > y else y

def max_num(function, nums):

    current_max = nums[0]
    for i in range(len(nums) -1):
        current_max = function(current_max, nums[i + 1])
    return current_max

print(max_num(bigger_num, numbers))