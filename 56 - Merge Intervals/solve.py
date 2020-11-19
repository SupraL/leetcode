class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        schedule = [intervals[0]]
        for i in intervals[1:]:
            last_schedule = schedule[-1]
            if i not in schedule:
                if last_schedule[0] <= i[0] <= last_schedule[1]:
                    last_schedule[1] = max(i[1], last_schedule[1])
                else:
                    schedule.append(i)
        return schedule