from enum import Enum
import cv2
from PIL import Image

class ImageType(Enum):
    UNKNOWN_TYPE = 0
    NUMPY = 1
    PILLOW = 2

    def __repr__(self):
        return "ImageType"

class ImageData:

    def __init__(self, data, tp = ImageType.NUMPY):
        """
        Image constructor
        `type` may be ImageType.NUMPY, ImageType.PILLOW
        """
        if isinstance (data, str):
            self.image_ = cv2.imread(data)
            self.image_ = cv2.cvtColor(self.image_, cv2.COLOR_BGR2RGB)
            self.type_ = ImageType.NUMPY
        else:
            self.type_ = tp
            self.image_ = data        

    def save(self, destination):
        """
        Save to designated path.
        """
        if self.type_ == ImageType.NUMPY:
            im_pil = Image.fromarray(self.image_)
        elif self.type_ == ImageType.PILLOW:
            im_pil = self.image_
        
        im_pil.save(destination)

    def to_pillow(self, inplace=False):
        """
        Convert to pillow type
        """
        if self.type_ == ImageType.NUMPY:
            im_pil = Image.fromarray(self.image_)
        elif self.type_ == ImageType.PILLOW:
            im_pil = self.image_

        if inplace:
            self.image_ = im_pil

        return ImageData(im_pil, ImageType.PILLOW)

    def to_numpy(self, inplace=False):
        """
        Convert to numpy type
        """
        if self.type_ == ImageType.NUMPY:
            im_np = self.image_
        elif self.type_ == ImageType.PILLOW:
            im_np = np.asarray(self.image_)

        if inplace:
            self.image_ = im_np

        return ImageData(im_np, ImageType.NUMPY)