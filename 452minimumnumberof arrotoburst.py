class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x:x[1])

        arrow=1
        prev_end= points[0][1]

        for start,end in points:

            if start>prev_end:
                arrow+=1
                prev_end= end
        return arrow
        
