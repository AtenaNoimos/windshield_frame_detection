import json


def read_json(json_file_path: str) -> dict:
    """takes a path to a json file and returns a contents

    Args:
        json_file_path (str): path to the json file

    Returns:
        dict: contents of the json file
    """
    f = open(json_file_path, "r")
    # Reading from file
    data = json.loads(f.read())
    return data


def merge_labelstudio_json_files(merged_file_name: str, *args: str):
    """merge mutiple json files

    Args:
        merged_file_name (str): the name of merged file (without .json)
    """
    merged_data = []
    for json in args:
        merged_data = merged_data + read_json(json)
    write_json(merged_data, merged_file_name)
    return merged_data


def write_json(data, json_file_name):
    """ writes the input data in a json file and save it in the current directory
    Args:
        data: input data
        json_file_name: the file name that should be saved (without .json postfix)"""

    json_file_name = json_file_name + ".json"
    if type(data) == dict:
        json_object = json.dumps(data, indent=4)
        with open(json_file_name, "w") as outfile:
            outfile.write(json_object)
    else:
        try:
            with open(json_file_name, "w") as outfile:
                outfile.write(data)
        except Exception:
            print("data type is not compatible with json write!")


def bounding_box(keypoints_list, image_size):
    points = [
        [keypoints_list[0], keypoints_list[1]],
        [keypoints_list[3], keypoints_list[4]],
        [keypoints_list[6], keypoints_list[7]],
        [keypoints_list[9], keypoints_list[10]],
    ]
    x_coordinates, y_coordinates = zip(*points)
    top_left_x = min(x_coordinates)
    top_left_y = min(y_coordinates)
    bottom_right_x = max(x_coordinates)
    bottom_right_y = max(y_coordinates)
    w = bottom_right_x - top_left_x
    h = bottom_right_y - top_left_y

    return [
        max(0, top_left_x - 50),
        max(0, top_left_y - 50),
        min(image_size[0], w + 100),
        min(image_size[0], h + 100),
    ]

