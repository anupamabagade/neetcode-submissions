class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        len_arr = len(arr)
        ans = [0] * len_arr
        for i in range(len_arr-1, -1, -1):
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)
        return ans
            
        