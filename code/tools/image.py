from enum import Enum
import cv2
import numpy as np
from PIL import Image
from copy import deepcopy

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
            self.image_ = deepcopy(data)        

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


    def make_gui_format(self):
        imgCV = self.to_numpy().image_
        imgCV = ImageData.image_resize(imgCV, height=300)
        frame = cv2.cvtColor(imgCV, cv2.COLOR_RGB2BGR)

        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        return imgbytes

    @staticmethod
    def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
        # initialize the dimensions of the image to be resized and
        # grab the image size
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = height / float(h)
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # resize the image
        resized = cv2.resize(image, dim, interpolation=inter)

        # return the resized image
        return resized
