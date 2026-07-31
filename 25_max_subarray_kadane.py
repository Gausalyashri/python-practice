"""Problem: Maximum Subarray Sum (Kadane's Algorithm)
Given an array of integers (possibly containing negative
numbers), find the contiguous subarray with the largest sum
and return that sum, in O(n) time.
"""

def max_subarray(nums):
    if not nums:
        return 0
    current_sum = best_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
