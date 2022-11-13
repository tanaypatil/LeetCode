#User function Template for python3
class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meetings = [Meeting(start[i], end[i]) for i in range(n)]
        meetings.sort(key=lambda x: x.end)
        # for m in meetings:
        #     print(m.start, m.end)
        limit = meetings[0].end
        count = 1
        for i in range(1, n):
            if meetings[i].start > limit:
                count += 1
                limit = meetings[i].end
        return count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends