class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l

s=Solution()
result=s.removeDuplicates([1,1,2,3,4,5,5])
print(result)
