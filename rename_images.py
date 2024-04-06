#-- Import --------------------------------------------------------------------
import os

#------------------------------------------------------------------------------
###############################################################################

def rename_files(imgs_dir, lbls_dir, img_format, base_name):
    
    image_files = [f for f in os.listdir(imgs_dir) if f.endswith(img_format)]
    counter = 1
    
    for img_file in image_files:        
        new_img_name = f'{base_name}_{counter}' + img_format
        os.rename(os.path.join(imgs_dir, img_file),
                  os.path.join(imgs_dir, new_img_name))
            
        lbl_file = os.path.splitext(img_file)[0] + '.txt'
        new_lbl_name = f'{base_name}_{counter}.txt' 
        os.rename(os.path.join(lbls_dir, lbl_file),
                  os.path.join(lbls_dir, new_lbl_name))    
            
        counter += 1        
###############################################################################

#-- Run -----------------------------------------------------------------------
imgs_dir = 'ds/ds_6/test/images'
lbls_dir = 'ds/ds_6/test/labels'
img_format = '.jpg'
base_name = 'ds_6'

rename_files(imgs_dir, lbls_dir, img_format, base_name)

#-- log --
print('finished :)')
#------------------------------------------------------------------------------