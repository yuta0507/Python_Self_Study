from typing import List

class Sort(object):
    def bubble(self, nums: List[int]) -> List[int]:
        """**Docstring Sample**
        Sort by bubble sort

        Args:
            nums (List[int]): Numbers that you want to sort
        Returns:
            List[int]
        """
        length = len(nums)

        for i in range(length):
            for j in range(length - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def cocktail(self, nums: List[int]) -> List[int]:
        swapped = True

        start = 0
        end = len(nums) - 1

        while True:
            swapped = False

            for i in range(start, end):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True

            if not swapped:
                break
            else:
                end = end - 1

            swapped = False

            for i in range(end, start, -1):
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    swapped = True

            if not swapped:
                break
            else:
                start = start + 1

        return nums



if __name__ == '__main__':
    sort = Sort()

    nums = [8, 5, 7, 3, 4, 6]
    print(sort.cocktail(nums))
