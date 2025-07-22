'''
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        maj=len(nums)//2
        for num in nums:
            count[num]=1+count.get(num,0)
            if count[num]>maj:
                return num

sol=Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))
