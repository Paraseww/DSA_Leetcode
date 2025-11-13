class Solution(object):
    def twoSum(self, nums, target):
        memory={}
        for i in range(len(nums)):
            num=nums[i]
            need=target-num
            if need in memory:
                return[memory[need],i]
            memory[num]=i
             

        