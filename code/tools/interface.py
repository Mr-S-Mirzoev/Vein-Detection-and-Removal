from filter import median_filter
import image

img = image.ImageData("/Users/polinakozuh/Desktop/IMG_1163.jpg")
mf = median_filter.MedianBlurFilter()
image_res = mf.apply(img)
image_res.save("here.jpg")