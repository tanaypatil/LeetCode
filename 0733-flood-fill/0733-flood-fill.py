from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return image
        m, n = len(image), len(image[0])
        
        visited = defaultdict(bool)
        q = deque({(sr, sc)})
        co = image[sr][sc]
        r = [1, -1, 0, 0]
        c = [0, 0, -1, 1]
        while q:
            i, j = q.popleft()
            # print(i, j)
            visited[(i, j)] = True
            for p in range(4):
                x, y = r[p] + i, c[p] + j
                if 0 <= x < m and 0 <= y < n and not visited[(x, y)] and image[x][y] == co:
                    q.append((x, y))
        # print(visited)
        for k, v in visited.items():
            image[k[0]][k[1]] = color if v else image[k[0]][k[1]]
        return image