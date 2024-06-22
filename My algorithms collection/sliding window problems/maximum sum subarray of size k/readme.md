Description:
Given an array of integers and a number k, find the maximum sum of a subarray of size k.

Example:
Input: [2, 1, 5, 1, 3, 2], k = 3
Output: 9 (subarray [5, 1, 3])

Hint:
Use a sliding window of size k to keep track of the sum of the current subarray. Slide the window from the start of the array to the end, updating the sum by subtracting the element that goes out of the window and adding the new element that comes into the window.