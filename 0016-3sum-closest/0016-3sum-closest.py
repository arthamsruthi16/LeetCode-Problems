class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = sum(nums[:3])
        n = len(nums)
        
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s == target:
                    return s  # cannot do better
                if abs(s - target) < abs(best - target):
                    best = s
                
                if s < target:
                    l += 1
                else:
                    r -= 1
        return best

        