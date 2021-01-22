from enum import Enum

import cv2

from filters import abstract_filter
from image import ImageData, ImageType

from PIL import Image

class MedianBlurFilter(abstract_filter.Filter):
    """
    Apply contrast stretching
    """

    def apply(self, inImage: ImageData):

        median_applied = MedianBlurFilter.filter_image(inImage)
        return ImageData(median_applied, ImageType.PILLOW)

    def __repr__(self):
        return 'MedianBlurFilter from code/tools/filer/median_filter.py'

    """
    Method to process the red band of the image
    """
    @staticmethod
    def normalizeRed(intensity):
        iI = intensity
        minI = 86
        maxI = 230
        minO = 0
        maxO = 255
        iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)

        return iO

    """
    Method to process the green band of the image
    """
    @staticmethod
    def normalizeGreen(intensity):
        iI = intensity
        minI = 90
        maxI = 225
        minO = 0
        maxO = 255
        iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)

        return iO

    """
    Method to process the blue band of the image
    """
    @staticmethod
    def normalizeBlue(intensity):
        iI = intensity
        minI = 100
        maxI = 210
        minO = 0
        maxO = 255
        iO = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)

        return iO

    """
    Worker for class logic
    """
    @staticmethod
    def filter_image(image: ImageData):
        # Create an image object
        imageObject = image.to_pillow().image_
        # Split the red, green and blue bands from the Image
        multiBands = imageObject.split()
        # Apply point operations that does contrast stretching on each color band
        normalizedRedBand = multiBands[0].point(
            MedianBlurFilter.normalizeRed)
        normalizedGreenBand = multiBands[1].point(
            MedianBlurFilter.normalizeGreen)
        normalizedBlueBand = multiBands[2].point(
            MedianBlurFilter.normalizeBlue)

        # Create a new image from the contrast stretched red, green and blue brands
        normalizedImage = Image.merge(
            "RGB",
            (
                normalizedRedBand,
                normalizedGreenBand,
                normalizedBlueBand
            )
        )

        return normalizedImage
