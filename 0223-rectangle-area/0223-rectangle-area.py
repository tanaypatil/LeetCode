class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2-ax1)*(ay2-ay1)
        area2 = (bx2-bx1)*(by2-by1)
        common = 0
        if ((ax1 <= bx1 <= ax2) or (ax1 <= bx2 <= ax2) or (bx1 <= ax1 <= bx2) or (bx1 <= ax2 <= bx2)) and ((ay1 <= by1 <= ay2) or (ay1 <= by2 <= ay2) or (by1 <= ay1 <= by2) or (by1 <= ay2 <= by2)):
            common = (min(ax2, bx2)-max(ax1, bx1)) * (min(ay2, by2)-max(ay1, by1))
        return area1+area2-common
        