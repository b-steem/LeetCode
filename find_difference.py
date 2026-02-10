class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique1 = set(nums1)
        unique2 = set(nums2)

        not_in2 = []
        not_in1 = []

        for num in unique1:
            if num not in unique2:
                not_in2.append(num)

        for num2 in unique2:
            if num2 not in unique1:
                not_in1.append(num2)

        return [not_in2, not_in1]