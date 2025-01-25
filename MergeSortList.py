class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1+=nums2
        nums1.sort()
        while 0 in nums1:
            nums1.remove(0)