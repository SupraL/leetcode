class Solution(object):
    def two_point_distance(self, p1, p2):
	    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        point_lst = [p1, p2, p3, p4]
        d_lst = []
        for i in range(len(point_lst)):
            for j in range(i+1, len(point_lst)):
                d_lst.append(self.two_point_distance(point_lst[i], point_lst[j]))
        d_lst.sort()
        return d_lst.count(d_lst[0]) == 4 and d_lst.count(d_lst[-1]) == 2