class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_distance(p1, p2):
            return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2
        distances = [get_distance(p1, p2), get_distance(p1, p3), get_distance(p1, p4), get_distance(p2, p3), get_distance(p2, p4), get_distance(p3, p4)]
        distances.sort()
        return (distances[0] == distances[1] == distances[2] == distances[3]) and (distances[4] == distances[5]) and (2*distances[0] == distances[4]) and (distances[0] != 0)