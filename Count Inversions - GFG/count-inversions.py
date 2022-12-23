class Solution:
    #User function Template for python3
    def mergeSort(self, arr):
        n = len(arr)
        if n == 1:
            return arr
        
        mid = n // 2 if not n % 2 else n//2 + 1
        
        left_sorted = self.mergeSort(arr[:mid])
        right_sorted = self.mergeSort(arr[mid:])
        left = right = 0
        sorted_arr = []
        while left < len(left_sorted) and right < len(right_sorted):
            if left_sorted[left] > right_sorted[right]:
                Solution.inversion_count += len(left_sorted)-left
                sorted_arr.append(right_sorted[right])
                right += 1
            else:
                sorted_arr.append(left_sorted[left])
                left += 1
                
        while left < len(left_sorted):
            sorted_arr.append(left_sorted[left])
            left += 1
            
        while right < len(right_sorted):
            sorted_arr.append(right_sorted[right])
            right += 1
            
        return sorted_arr
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        Solution.inversion_count = 0
        self.mergeSort(arr)
        return Solution.inversion_count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends