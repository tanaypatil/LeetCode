class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-count for count in Counter(tasks).values()]
        heapify(heap)
        
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                count = 1 + heappop(heap)
                if count != 0:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heappush(heap, q.popleft()[0])
        return time
        