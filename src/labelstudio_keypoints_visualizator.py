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
        image_path = os.path.join(image_dir, img_name)
        image_path = image_dir+ img_name
        image_save_path = os.path.join(image_save_dir, img_name)
        image_save_path = image_save_dir+ img_name
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
            
        image_keypoints[img_name]=points_dict
        
        cv2.imwrite(image_save_path, img)
    return image_keypoints_dict