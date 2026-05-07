class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            nums1,nums2 = nums2,nums1

        
        lo,hi = 0,len(nums1)-1

        total = len(nums1)+len(nums2)
        half = total // 2
        while True:
            mid = (lo+hi)//2
            right = half - mid -2


            nleft = nums1[mid] if mid>=0 else float('-inf')
            nright = nums1[mid+1] if mid+1 < len(nums1) else float('inf')
            n1left = nums2[right] if right>=0 else float('-inf')
            n1right = nums2[right+1] if right+1 < len(nums2) else float('inf')


            if nleft <= n1right and nleft <= nright:
                if total %2:
                    return min(nright,n1right)
                return (max(nleft,n1left) + min(nright,n1right))/2
            elif nleft > n1right:
                hi = mid-1
            else:
                lo = mid+1