class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Range - [0, 1, 2]
        counts = [0,0,0]
        for i in range(len(nums)):
            counts[nums[i]] += 1

        ind = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[ind] = i
                ind += 1