#-- Import --------------------------------------------------------------------
import os

#------------------------------------------------------------------------------
###############################################################################

#-- Run -----------------------------------------------------------------------
imgs_dir = 'ds/ds_7/images/'
lbls_dir = 'ds/ds_7/labels/'
img_format = '.JPEG'

#-- Get a list of all image files --
image_files = [f for f in os.listdir(imgs_dir) if f.endswith(img_format)]

#-- Iterate through each image file --
for img_file in image_files:
    
    lbl_file = os.path.splitext(img_file)[0] + '.txt'    
    
    if not os.path.exists(os.path.join(lbls_dir, lbl_file)):
        
        # If not exist, create an empty text file
        with open(os.path.join(lbls_dir, lbl_file), 'w') as file:
            pass  # This line does nothing, creating an empty text file

#-- log --
print('finished :)')
#------------------------------------------------------------------------------