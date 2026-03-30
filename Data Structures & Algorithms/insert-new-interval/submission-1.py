class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # I prefer to create a new result for it
        # sorted
        # which to insert? iterate through the intervals and find the index i where newInterval[0]>=intervals[i][0]
        # after we found the spot? 
        #   let old_start = intervals[i][0]
        #   let old_end = intervals[i][1]
        #   let new_start = newIntervals[0]
        #   let new_end = newIntervals[1]
        #   if old_end<new_start:
        #       if i+1== n or new_end <intervals[i+1][0]:
        #           add newInterval, no need to merge
        #       else:
        #           add[new_start, intervals[i+1][1]] to the result
        #           added = True break the loop
        #   else
        #       if intervals[i][1]<=newIntervals[1]
        #           i+=1
        #           continue
        #       add  [old_start, new_end] to the result
        n = len(intervals)
        result = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        added = False
        i = 0
        while i<n:
            old_start = intervals[i][0]
            old_end = intervals[i][1]
            if not added and new_end < old_start:
                result.append([new_start,new_end])
                added = True
            if added or old_end < new_start:
                result.append(intervals[i])
            else:
                new_start = min(old_start,new_start)
                new_end = max(old_end,new_end)
            i+=1

        if not added:
            result.append([new_start, new_end])

        return result
                # insert = [6,7]
                # old_pair=[3,6]
                # 


        