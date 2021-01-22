from matplotlib import pyplot as plt
import json
import numpy as np
from enum import Enum

import cv2

from filter import abstract_filter
from image import ImageData, ImageType

from PIL import Image

class EqualizeFilter(abstract_filter.Filter):
    def __init__(self, gray=False):
        self.gray_ = gray

    def apply(self, inImage: ImageData):

        equalize_applied = EqualizeFilter.equalize_this(inImage, gray_scale=self.gray_)

        if self.gray_:
            equalize_applied = cv2.cvtColor(equalize_applied, cv2.COLOR_GRAY2RGB)
            
        return ImageData(equalize_applied, ImageType.NUMPY)

    def __repr__(self):
        return '{}EqualizeFilter from code/tools/filer/equalizer_filter.py'.format('Gray' if self.gray_ else "")

    @staticmethod
    def read_this(image_file: ImageData, gray_scale=False):
        image_src = image_file.to_numpy().image_
        if gray_scale:
            image_src = cv2.cvtColor(image_src, cv2.COLOR_RGB2GRAY)

        return image_src

    @staticmethod
    def equalize_this(image_file: ImageData, with_plot=False, gray_scale=False):
        image_src = EqualizeFilter.read_this(image_file=image_file, gray_scale=gray_scale)
        if not gray_scale:
            r_image, g_image, b_image = cv2.split(image_src)

            r_image_eq = cv2.equalizeHist(r_image)
            g_image_eq = cv2.equalizeHist(g_image)
            b_image_eq = cv2.equalizeHist(b_image)

            image_eq = cv2.merge((r_image_eq, g_image_eq, b_image_eq))
            cmap_val = None
        else:
            image_eq = cv2.equalizeHist(image_src)
            cmap_val = 'gray'

        if with_plot:
            fig = plt.figure(figsize=(10, 20))

            ax1 = fig.add_subplot(2, 2, 1)
            ax1.axis("off")
            ax1.title.set_text('Original')
            ax2 = fig.add_subplot(2, 2, 2)
            ax2.axis("off")
            ax2.title.set_text("Equalized")

            ax1.imshow(image_src, cmap=cmap_val)
            ax2.imshow(image_eq, cmap=cmap_val)

        return image_eq
