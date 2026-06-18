class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # Place each number in its correct index if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find the first place where index doesn't match value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all are in place, then the answer is n+1
        return n + 1
