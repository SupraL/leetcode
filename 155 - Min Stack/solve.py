class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num_lst = []
        self.min_lst = []
        self.current_min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.current_min == None:
            self.min_lst.insert(len(self.min_lst), x)
            self.current_min = x
        else:
            if x < self.current_min:
                self.current_min = x
                self.min_lst.insert(len(self.min_lst), x)
            else:
                self.min_lst.insert(len(self.min_lst), self.current_min)
        self.num_lst.insert(len(self.num_lst), x)
        

    def pop(self):
        """
        :rtype: None
        """
        out = self.num_lst[-1]
        del self.num_lst[-1]
        del self.min_lst[-1]
        if len(self.num_lst) == 0:
            self.current_min = None
        else:
            self.current_min = self.min_lst[-1]
        return out
        

    def top(self):
        """
        :rtype: int
        """
        return self.num_lst[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.current_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()