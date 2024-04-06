#-- Import --------------------------------------------------------------------
import cv2
import matplotlib.pyplot as plt

import os
import shutil

import random

#------------------------------------------------------------------------------
###############################################################################

#-- Set path --
imgs_dir = 'ds/ds_6/test/images'
lbls_dir = 'ds/ds_6/test/labels/'
backs_dir = 'ds/background_images'
img_format = '.jpg'


#-- Get a list of image file names and label file names --
image_files = [f for f in os.listdir(imgs_dir) if f.endswith(img_format)]
label_files = [f for f in os.listdir(lbls_dir) if f.endswith('.txt')]

#-- count number of background images --
back_list = []

for lbl_file in label_files:
    lbl_path = os.path.join(lbls_dir, lbl_file)
    
    if os.path.getsize(lbl_path) == 0:        
        back_list.append(lbl_file)
        
        #-- move background images to backs_dir --
        img_file = os.path.splitext(lbl_file)[0] + img_format
        img_path = os.path.join(imgs_dir, img_file)
        
        dest_lbl_path = os.path.join(backs_dir, lbl_file)
        dest_img_path = os.path.join(backs_dir, img_file)        
        
        shutil.move(img_path, dest_img_path)
        shutil.move(lbl_path, dest_lbl_path)
        
        
    
        


print(f'Number of Background Images: {len(back_list)}')    

# #-- Plot Background Images --
# for lbl_file in back_list:       
#     img_file = os.path.splitext(lbl_file)[0] + img_format
#     img_path = os.path.join(imgs_dir, img_file)

#     #-- Read image --
#     image = cv2.imread(img_path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #-- Convert from BGR to RGB
    
#     #-- Show image --
#     plt.axis('off')
#     plt.title(img_file)
#     plt.imshow(image)
#     plt.show()

print('finished! :)')
#---------------------------------------------------------------------------------------------------------------

