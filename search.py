from typing import List

def binary(nums: List[int], search: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (right + left) // 2

        if search == nums[middle]:
            return middle
        elif search < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1


if __name__ == '__main__':
    nums = [1, 3, 5, 10, 15, 18, 21]
    print(binary(nums, 1))
