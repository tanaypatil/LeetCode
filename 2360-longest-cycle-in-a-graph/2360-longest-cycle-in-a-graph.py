class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = defaultdict(bool)
        rec = defaultdict(bool)
        ans = [-1]
        
        def dfs(i):
            visited[i] = True
            rec[i] = True
            # print(i)
            
            time[0] += 1
            curr[i] = time[0]
            
            if edges[i] >= 0:
                if not visited[edges[i]]:
                    dfs(edges[i])
                elif rec[edges[i]]:
                    # print("here")
                    # print(curr, time, time[0]+1-curr[edges[i]])
                    ans[0] = max(ans[0], time[0]+1-curr[edges[i]])
                    # print(ans[0])
            
            rec[i] = False
            
        for i in range(len(edges)):
            if not visited[i]:
                curr = defaultdict(int)
                time = [0]
                dfs(i)
        
        return ans[0]