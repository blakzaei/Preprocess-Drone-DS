#-- Import --------------------------------------------------------------------
import xml.etree.ElementTree as ET
import os
#------------------------------------------------------------------------------
###############################################################################


#-- Function to convert XML annotations to YOLO format ------------------------
def convert_xml_to_yolo(xml_folder, output_folder, class_map):
    for filename in os.listdir(xml_folder):
        if filename.endswith('.xml'):
            xml_path = os.path.join(xml_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')
            tree = ET.parse(xml_path)
            root = tree.getroot()
            size = root.find('size')
            width = int(size.find('width').text)
            height = int(size.find('height').text)
            
            with open(output_path, 'w') as f:
                for obj in root.findall('object'):
                    class_name = obj.find('name').text
                    if class_name not in class_map:
                        print(f'Class {class_name} not found in class map. Skipping.')
                        continue
                    class_id = class_map[class_name]
                    bbox = obj.find('bndbox')
                    xmin = int(bbox.find('xmin').text)
                    ymin = int(bbox.find('ymin').text)
                    xmax = int(bbox.find('xmax').text)
                    ymax = int(bbox.find('ymax').text)
                    x_center = (xmin + xmax) / (2.0 * width)
                    y_center = (ymin + ymax) / (2.0 * height)
                    bbox_width = (xmax - xmin) / width
                    bbox_height = (ymax - ymin) / height
                    f.write(f'{class_id} {x_center} {y_center} {bbox_width} {bbox_height}\n')
#------------------------------------------------------------------------------
###############################################################################


#-- Run -----------------------------------------------------------------------
xml_folder = 'ds/ds_1/ds_1_test/labels_xml/'
output_folder = 'ds/ds_1/ds_1_test/labels/'
class_map = {'drone': 0}  
convert_xml_to_yolo(xml_folder, output_folder, class_map)

#-- log --
print('finished :)')

#------------------------------------------------------------------------------
