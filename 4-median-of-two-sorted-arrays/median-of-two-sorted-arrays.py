class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        low, high = 0, m

        while low <= high:
            cutA = (low + high) // 2
            cutB = (m + n + 1) // 2 - cutA

            leftA = float('-inf') if cutA == 0 else A[cutA - 1]
            rightA = float('inf') if cutA == m else A[cutA]

            leftB = float('-inf') if cutB == 0 else B[cutB - 1]
            rightB = float('inf') if cutB == n else B[cutB]

            if leftA <= rightB and leftB <= rightA:
                if (m + n) % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                else:
                    return max(leftA, leftB)
            elif leftA > rightB:
                high = cutA - 1
            else:
                low = cutA + 1
