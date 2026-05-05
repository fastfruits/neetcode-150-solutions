class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): #search smallest array
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        half = (m + n + 1) // 2
        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]

            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1: #valid partition
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif maxLeft1 > minRight2:
                right = i - 1 #i too big so move left
            else:
                left = i + 1 #i too small so move right