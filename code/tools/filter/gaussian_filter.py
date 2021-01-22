import numpy as np
import scipy.ndimage as ndimage

from filter import abstract_filter
from image import ImageData, ImageType


class GaussianFilter(abstract_filter.Filter):

    def apply(self, inImage: ImageData):

        img = inImage.to_numpy().image_

        # Note the 0 sigma for the last axis, we don't wan't to blurr the color planes together!
        img = ndimage.gaussian_filter(img, sigma=(5, 5, 0), order=0)

        return ImageData(img, ImageType.NUMPY)

    def __repr__(self):
        return 'GaussianFilter from code/tools/filer/gaussian_filter.py'
