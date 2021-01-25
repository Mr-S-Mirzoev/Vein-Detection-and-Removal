from copy import deepcopy
from image import ImageData

class FilterPipe:
    """
    A factory of filters
    """
    
    def __init__(self, vector):
        self.pipeline_ = deepcopy(vector)

    def work(self, source: ImageData):
        inp = deepcopy(source)
        out = None
        
        print("Running image through a pipeline")

        for filt in self.pipeline_:
            out = filt.apply(inp)
            print("Running on: {}".format(filt))
            inp = out

        print()

        return deepcopy(out)