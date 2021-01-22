import cv2

from filter import abstract_filter
from image import ImageData, ImageType


class GausianFilter(abstract_filter.Filter):

    def apply(self, inImage: ImageData):

        blur = cv2.GaussianBlur(inImage.to_numpy(), (5, 5), 3)

        return ImageData(blur, ImageType.NUMPY)

    def __repr__(self):
        return 'GausianFilter from code/tools/filer/equalizer_filter.py'.format('Gray' if self.gray_ else "")

    @staticmethod
    def worker(image_file: ImageData,
                      #with_plot=False,
                      gray_scale=False):

        return image_eq
