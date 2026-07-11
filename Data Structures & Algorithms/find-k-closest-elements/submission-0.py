class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l, r = 0, len(arr) - 1
        #[l: r + 1]

        while r - l + 1 > k:
            left_distance = abs(arr[l] - x)
            right_distance = abs(arr[r] - x)

            if left_distance > right_distance:
                l += 1
            else:
                r -= 1
        
        return arr[l: r + 1]