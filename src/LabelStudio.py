import json
import os
import cv2
import math 
from datetime import datetime
from utils import read_json, write_json

def plot_labelstudio_keypoints(json_file_path, read_img_dir, write_img_dir):
    """ a function to read keypoints lables in Label studio jso format and visualized them on the images
    Args:
        json_file_path: path to the json file
        read_img_dir: the directory where all images are there
        write_img_dir: the directory where results will be saved
        
    Returns:
        image_keypoints_dict: a dictionary like {img_name: {'keypointlabel1': (x1,y1), 'keypointlabel2': (x2,y2), ...}}
    """
    f = open (json_file_path, "r")
    data = json.loads(f.read())
    image_keypoints_dict= {}
    for idx, image in enumerate(data):
        img_points ={}
        img_name = image["data"]['img'].split("/")[-1].split("-", maxsplit=1)[-1]
        image_path = os.path.join(read_img_dir, img_name)
        image_save_path = os.path.join(write_img_dir, img_name)
        img =cv2.imread(image_path)
        annotation = image ['annotations'][0]['result']
        points_dict = {}
        for cnt, point in enumerate(annotation):
            label = point['value']['keypointlabels'][0]
            x = point['value']['x']
            y = point['value']['y']
            original_width= point["original_width"]
            original_height= point["original_height"]
            points_dict[label]=(math.floor(x*original_width/100),math.floor((y)*original_height/100))
            radius= 3
            if label == "lower_right":
                img = cv2.circle(img, (points_dict[label][0], points_dict[label][1]), radius, (255, 0, 0), -1)
            elif label == "lower_left":
                img = cv2.circle(img, (points_dict[label][0], points_dict[label][1]), radius, (0, 0, 255), -1)
            elif label == "top_right":
                img = cv2.circle(img, (points_dict[label][0], points_dict[label][1]), radius, (0, 255, 137), -1)
            elif label == "top_left":
                img = cv2.circle(img, (points_dict[label][0], points_dict[label][1]), radius, (188, 255, 0), -1)
            
        
        cv2.imwrite(image_save_path, img)
    return image_keypoints_dict
    
    
    
def labelstudio_to_coco_convertor_keypoints(LabelStudio_json_file_path, Coco_json_file_name):
    """ a function which converts a label studio json file to a coco json file and save the results in a json in the current directory file
        Args:
            LabelStudio_json_file_path: path to the label studio json file
            Coco_json_file_name : the name of coco_json file
            
        Returns:
            coco_dict: data in coco format """
            
    data = read_json(LabelStudio_json_file_path)
    #f = open (json_file_name, "r")
    # Reading from file
    #data = json.loads(f.read())
    coco_dict = {}
    coco_dict["info"] = dict(description=None, ulr=None, version=None, year=2019, contributor=None, data_created=datetime.now().strftime("%m/%d/%Y, %H:%M") )
    coco_dict["licences"] = dict(ulr=None, id=0, name=None)
    coco_dict["images"] =[]
    coco_dict["annotations"] =[]
    coco_dict["categories"] = dict(supercategory="windshield", id = 1, name = "windshield",keypoints = ["lower_left", "top_left","top_right","lower_right"],
                              skeleton = [[1,2], [2,3], [3,4], [4,1]])
    image_dir = "../data/first_100samples/100_Samples"
    img_id = 0
    for idx, image in enumerate(data):
        img_name = image["data"]['img'].split("/")[-1].split("-", maxsplit=1)[-1]
        annotation = image ['annotations'][0]['result']
        points_dict = {}
        keypoint_list = [0,0,0, 0,0,0, 0,0,0, 0,0,0]
        for cnt, point in enumerate(annotation):
            label = point['value']['keypointlabels'][0]
            x = point['value']['x']
            y = point['value']['y']
            original_width= point["original_width"]
            original_height= point["original_height"]
            x = math.floor(x*original_width/100)
            y = math.floor(y*original_height/100)
            if label == "lower_left":
                keypoint_list[0] = x
                keypoint_list[1] = y
                keypoint_list[2] = 2
            
            elif label == "top_left":
                keypoint_list[3] = x
                keypoint_list[4] = y
                keypoint_list[5] = 2
            elif label == "top_right":
                keypoint_list[6] = x
                keypoint_list[7] = y
                keypoint_list[8] = 2
            elif label == "lower_right":
                keypoint_list[9] = x
                keypoint_list[10] = y
                keypoint_list[11] = 2
            
        annotation_dict = dict(keypoints = keypoint_list, num_keypoints = cnt+1,
                                image_id= img_id, category_id=0)
        coco_dict["annotations"].append(annotation_dict)
        img_dict=dict(license =0, ulr=None, file_name=img_name,height=original_height, width=original_width, id = img_id)
        coco_dict["images"].append(img_dict)
        img_id+=1
        write_json(coco_dict, Coco_json_file_name)
        
        
    return coco_dict