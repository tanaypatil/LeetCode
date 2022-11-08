#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        left = 0
        freq = {}
        res = 0
        for right, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            if len(freq) == k:
               res = max(res, right-left+1) 
            while len(freq) > k:
                freq[s[left]] -= 1
                if not freq[s[left]]:
                    del freq[s[left]]
                left += 1
        return res if res else -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends