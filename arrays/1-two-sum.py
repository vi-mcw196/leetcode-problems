from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # first brute-force approach
    """
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    O(n^2) time complexity
    O(1) space complexity
    """

    # second approach (using map)
    # O(n) time complexity
    # O(n) space complexity
    num_to_index_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index_map:
            return [num_to_index_map[complement], index]
        num_to_index_map[num] = index


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]
