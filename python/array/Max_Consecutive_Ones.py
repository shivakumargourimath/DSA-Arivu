'''
LeetCode 485. Max Consecutive Ones
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
             The maximum number of consecutive 1s is 3.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        max_cnt=0
        for num in nums:
            if num==1:
                cnt+=1
                max_cnt=max(cnt,max_cnt)
            else:
                cnt=0
        return max_cnt

s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # Output: 3

#using while loop

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        max_cnt=0
        r=0
        while r<len(nums):
            if nums[r]==1:
                cnt+=1
                max_cnt=max(cnt,max_cnt)
            else:
                cnt=0
            r+=1
        return max_cnt

s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # Output: 3
