class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)

        # precompute char to index map for the target str
        tgt_c_to_idx = collections.defaultdict(list)
        for i, c in enumerate(s2):
            tgt_c_to_idx[c].append(i)

        q = collections.deque([(0, s1)]) # steps (int), node (str)
        seen = set()
        seen.add(s1)
        while q:
            k, u = q.popleft()
            if u == s2:
                return k
            for i in range(n - 1):
                if u[i] == s2[i]: continue
                for j in tgt_c_to_idx[u[i]]:
                    if j <= i: continue
                    # swap i and j, construct neighbor v
                    v = list(u)
                    v[i], v[j] = v[j], v[i]
                    v = ''.join(v)
                    if v not in seen:
                        seen.add(v)
                        q.append((k + 1, v))
                break
        