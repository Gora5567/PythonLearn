from functools import reduce


def product_list(nums):
    return reduce(lambda x, y: x * y, nums)
