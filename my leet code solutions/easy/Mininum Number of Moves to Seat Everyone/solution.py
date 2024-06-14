# class Solution(object):
#     def minMovesToSeat(self, seats, students):
#         """
#         :type seats: List[int]
#         :type students: List[int]
#         :rtype: int
#         """
#         seats = sorted(seats)
#         students = sorted(students)
#         move_no = [abs(i -j) for i, j in zip(seats, students)]
#         return sum(move_no)




def merge(nums1, m, nums2, n):
    nums1 = nums1[:m]
    nums2 = nums2[:n]
    i = 0
    while i < m:
        j = 0

        for  _ in range(n):
            # print((nums2[j], nums1[i], j, i))
            if nums2[j] < nums1[i]:
                print('got here')
                
                nums1.insert(i, nums2[j])
                # print('nums: ', nums1)
                j += 1
                break
        i += 1
    nums1 += nums2[j+1:]
    print(j+1)
    print(n)
    return nums1

print(merge([1,2,3,0,0,0], 3, [3,4,5, 0,0], 3))