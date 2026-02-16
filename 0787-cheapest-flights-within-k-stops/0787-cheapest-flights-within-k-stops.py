class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for i, j, p in flights:
            adj[i].append((j, p))

        seenstops = {}
        heap = [(0, k, src)]

        while heap:
            price, stops, city = heappop(heap)

            if city == dst:
                return price

            if stops < 0:
                continue

            if city in seenstops and seenstops[city] >= stops:
                continue

            seenstops[city] = stops

            for next_city, next_price in adj[city]:
                heappush(heap, (price+next_price, stops-1, next_city))

        return -1