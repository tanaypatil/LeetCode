#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p-1)
            self.quickSort(arr, p+1, high)
    
    def partition(self,arr,low,high):
        # code here
        pivot = arr[low]
        l, r = low + 1, high
        while l <= r:
            if arr[l] <= pivot:
                l += 1
            if arr[r] >= pivot:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
        arr[low], arr[r] = arr[r], arr[low]
        return r


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends