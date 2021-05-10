class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr, l, r, x):
            # Check base case
            if r >= l:
                mid = l + (r - l) // 2

                # If element is present at the middle itself
                if arr[mid] == x:
                    return mid

                # If element is smaller than mid, then it
                # can only be present in left subarray
                elif arr[mid] > x:
                    return binarySearch(arr, l, mid-1, x)

                # Else the element can only be present
                # in right subarray
                else:
                    return binarySearch(arr, mid + 1, r, x)

            else:
                # Element is not present in the array
                return -1
        for i in range(len(matrix)):
            if not target > matrix[i][-1]:
                a = binarySearch(matrix[i], 0, len(matrix[i])-1, target)
                return a != -1
        return False
        