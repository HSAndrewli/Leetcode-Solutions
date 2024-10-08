
def search(nums, target) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (right + left) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1

print(search([-1, 0, 3, 5, 9, 12], 9))

# Time Complexity: O(log(n))
# Space Complexity: O(1)
