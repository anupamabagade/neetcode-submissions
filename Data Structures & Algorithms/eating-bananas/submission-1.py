class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Performing binary search on range of k

        left = 1
        right = max(piles)
        
        res = max(piles)

        while left <= right :
            k = (left + right) // 2
            hours = 0
            for p in piles :
                hours += math.ceil(p/k)
                
            if hours <= h :
                res = min(res,k)
                right = k - 1
            else :
                left = k + 1
        
        return res