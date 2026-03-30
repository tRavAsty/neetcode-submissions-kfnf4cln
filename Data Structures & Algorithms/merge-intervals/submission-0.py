class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda pair:pair[0])
        cur_start,cur_end = intervals[0][0],intervals[0][1]

        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            if start>cur_end:
                res.append([cur_start,cur_end])
                cur_start = start
                cur_end = end
            else:
                cur_start = min(cur_start,start)
                cur_end = max(cur_end,end)
        res.append([cur_start,cur_end])
        return res


        