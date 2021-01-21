from copy import deepcopy

class FilterPipe:
    """
    A factory of filters
    """
    
    def __init__(self, vector):
        self.pipeline_ = deepcopy(vector)

    def work(self, source, destination):
        inp = 
        for 