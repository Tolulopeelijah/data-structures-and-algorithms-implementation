class Solution():
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        self.nums1 = nums1[:m]
        self.nums2 = nums2[:n]
        i = 0
        j = 0
        while i < m:
            j = 0
            while j < n:
                if self.nums2[j] < self.nums1[i]:
                    self.nums1.insert(i, self.nums2[j])
                    break
                j += 1
            i += 1
        self.nums1 += self.nums2[j+1:n]
        return self.nums1


m = Solution()
print(m.merge([1,2,3,0,0], 3, [2,4,5], 3))