from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = list(map(int, input("nums = ").split()))
target = int(input("target = "))
print(twoSum(nums, target))
