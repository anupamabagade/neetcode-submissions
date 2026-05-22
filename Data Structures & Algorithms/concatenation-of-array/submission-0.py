class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #ans = [0] = len(2*n)
        ans = nums + nums
        return ans