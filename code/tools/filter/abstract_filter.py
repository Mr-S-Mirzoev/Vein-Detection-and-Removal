import image

class Filter:
    """
    Abstract class, representing Filters
    """
    
    def __init__(self):
        """
        Constructor
        """
        pass

    def apply(self, image: image.ImageData):
        """
        Apply a filter to the `image`
        """
        raise NotImplementedError

    def save(self, path, image):
        """
        Save the result to the path
        """
        raise NotImplementedError