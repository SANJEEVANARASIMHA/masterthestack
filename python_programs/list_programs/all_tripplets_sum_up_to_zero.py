def three_sum(nums):
    nums.sort()  # Sort the list first
    triplets = set()

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
    return list(triplets)


example_list = [-1, 0, 1, 2, -1, -4]
print(three_sum(example_list))
