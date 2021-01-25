from __future__ import print_function
from PIL import Image, ImageDraw
import json
import imageio
import cv2
import imutils
import argparse
import numpy as np
from imutils import contours
from imutils import perspective

import shutil
import os

"""
filepath = 'PennFudanPed/PNGImages/FudanPed00002.png'
database_name = "Vein Varicose database"
height, width, channels = imageio.imread(filepath).shape
quantity = 1
labels = [
    ''
]
concatenated_list = "\"hello\""
"""

def make_text(filepath, width, height, channels, quantity, bb_list, pixmap):

    filetext = "# Compatible with PASCAL Annotation Version 1.00\n"

    filetext += "Image filename : \"{}\"".format(filepath) + '\n'
    filetext += "Image size (X x Y x C) : {} x {} x {}".format(
        width, 
        height, 
        channels
    ) + '\n'
    filetext += "Database : \"{}\"".format(database_name) + '\n'
    filetext += "Objects with ground truth: %d { " % quantity
    for i in range(quantity):
        filetext += "\"{}\" ".format("Vein")
    filetext += "}\n# Note there may be some objects not included in the ground truth list for they are severe-occluded"
    filetext += "\n# or have very small size.\n# Top left pixel co-ordinates : (1, 1)\n"
    for i in range(quantity):
        filetext += "# Details for vein %d (\"Vein\")" % (i + 1) + '\n'
        filetext += "Original label for object %d \"Vein\" : \"VaricoseVein\"" % (i + 1) + '\n'
        filetext += "Bounding box for object {} \"Vein\" (Xmin, Ymin) - (Xmax, Ymax) : ({}, {}) - ({}, {})".format(
            i + 1,
            bb_list[i][0][0],
            bb_list[i][0][1],
            bb_list[i][1][0],
            bb_list[i][1][1]
        ) + '\n'
        filetext += "Pixel mask for object {} \"Vein\" : \"{}\"".format(
            i + 1,
            pixmap
        ) + "\n\n"

    return filetext

def order_points_old(pts):
	# initialize a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype="float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis=1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis=1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return rect

prefix = "/home/sergey/db/"
photos_prefix = "/home/sergey/Projects/Vein-Detection-and-Removal/datasets/photos/"

pix_map_short_pref = "PennFudanPed/PedMasks/"
img_short_pref = "PennFudanPed/PNGImages/"
annots_short_pre = "PennFudanPed/Annotations/"

index = 0
with open("via_region_data.json") as json_file:
    data = json.load(json_file) 

    for value in data:
        image = data[value]
        f_name = image["filename"]
        
        filepath = photos_prefix + f_name
        database_name = "Vein Varicose database"
        height, width, channels = imageio.imread(filepath).shape

        img = Image.new('L', (width, height), 0)

        quantity = len(image["regions"])
        bb_list = list()

        for i in range(quantity):
            x_coords = image["regions"][str(i)]["shape_attributes"]["all_points_x"]
            y_coords = image["regions"][str(i)]["shape_attributes"]["all_points_y"]

            polygon = [(x_coords[i], y_coords[i]) for i in range(len(x_coords))]
            
            ordered_dots = order_points_old(np.asarray(polygon))
            
            leftmost_up = ordered_dots[0]
            rightmost_down = ordered_dots[2]

            # polygon = [(x1,y1),(x2,y2),...] or [x1,y1,x2,y2,...]
            # width = ?
            # height = ?
            bb_list.append((leftmost_up, rightmost_down))

            ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)

        if quantity:
            pix_map_path = pix_map_short_pref + "FudanPed{}.png".format(index)
            image_path = img_short_pref + "FudanPed{}.png".format(index)
            annot_path = annots_short_pre + "FudanPed{}.txt".format(index)

            img.save(prefix + pix_map_path)
            src_dir = photos_prefix
            dst_dir = prefix + img_short_pref
            imageNames = list()
            imageNames.append(f_name)
            for imageName in imageNames:
                shutil.copy(os.path.join(src_dir, imageName),
                            os.path.join(dst_dir, "FudanPed{}.png".format(index)))

            file_text = make_text(f_name, width, height, channels, quantity, bb_list, pix_map_path)
            
            annots_fullpath = prefix + annot_path
            text_file=open(annots_fullpath, "w")
            text_file.write(file_text)
            text_file.close()

            index += 1
            
