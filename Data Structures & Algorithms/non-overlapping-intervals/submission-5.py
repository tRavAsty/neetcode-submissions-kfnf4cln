class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[0])
        res = 0
        prev_end = intervals[0][1]
        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            if start < prev_end:
                res += 1
                if end < prev_end:
                    prev_end = end
            else:
                prev_end = end
        return res
                
        