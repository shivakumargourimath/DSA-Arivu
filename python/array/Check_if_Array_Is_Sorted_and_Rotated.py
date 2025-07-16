class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        cnt=0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                cnt+=1
                if cnt>1:
                    return False
        return True

sol = Solution()

# Test cases
print(sol.check([3, 4, 5, 1, 2]))  # True (rotated sorted)
print(sol.check([2, 1, 3, 4]))     # False (not rotated sorted)
print(sol.check([1, 2, 3, 4, 5]))  # True (already sorted)
