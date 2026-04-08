class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0,0


        # while fast < len(nums):
        #     print(fast,slow)
        #     if nums[slow] == nums[fast]:
        #         return nums[slow]
            
        #     slow+=1
        #     fast+=2

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        

        s2 = 0
        while True:
            slow = nums[slow]
            s2 = nums[s2]
            if slow==s2:
                return slow
        
        return -1