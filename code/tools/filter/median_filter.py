from enum import Enum

import cv2

from filter import abstract_filter
from image import ImageData, ImageType

class MedianBlurFilter(abstract_filter.Filter):
    def apply(self, inImage: ImageData):

        image = inImage.to_numpy().image_
        blur = cv2.medianBlur(image, 5)
        return ImageData(blur, ImageType.NUMPY)