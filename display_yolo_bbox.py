#-- Import --------------------------------------------------------------------
import cv2
from IPython import display
import matplotlib.pyplot as plt

import shutil
import os

import random

#------------------------------------------------------------------------------
###############################################################################



# Function to draw bounding boxes on an image ---------------------------------
def draw_bboxes(image, bboxes):
    for bbox in bboxes:
        x, y, w, h = bbox
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image
#------------------------------------------------------------------------------

#-- Function to read and convert bounding box coordinates ---------------------
def read_bboxes(file_path, img_shape):
    with open(file_path, 'r') as file:
        bboxes = []
        for line in file:
            # YOLO format: class, x_center, y_center, width, height (normalized)
            class_id, x_center, y_center, width, height = map(float, line.strip().split())
            x_center, y_center = x_center * img_shape[1], y_center * img_shape[0]
            width, height = width * img_shape[1], height * img_shape[0]
            x, y = int(x_center - width / 2), int(y_center - height / 2)
            bboxes.append([int(x), int(y), int(width), int(height)])
    return bboxes
#------------------------------------------------------------------------------
###############################################################################


#-- show a few random images with bounding boxes ------------------------------

#-- Set path --
imgs_dir = 'ds/ds_8/images'
lbls_dir = 'ds/ds_8/labels'
img_format = '.png'

#-- Get a list of image file names --
image_files = [f for f in os.listdir(imgs_dir) if f.endswith(img_format)]
random.shuffle(image_files)



#-- Select a few random images --
num_of_img = 10
selected_images = image_files[:num_of_img]

#-- Plot Images --
for img_file in selected_images:
    img_path = os.path.join(imgs_dir, img_file)
    bbox_path = os.path.join(lbls_dir, os.path.splitext(img_file)[0] + '.txt')

    #-- Read image --
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #-- Convert from BGR to RGB
    img_shape = image.shape

    #-- Read and draw bounding boxes --
    bboxes = read_bboxes(bbox_path, img_shape)
    image_with_bboxes = draw_bboxes(image.copy(), bboxes)

    #-- Show images --
    plt.axis('off')
    plt.title(img_file)
    plt.imshow(image_with_bboxes)
    plt.show()
#---------------------------------------------------------------------------------------------------------------

