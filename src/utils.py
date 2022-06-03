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

    # if (
    #     keypoints_list[2]
    #     == 2 & keypoints_list[5]
    #     == 2 & keypoints_list[8]
    #     == 2 & keypoints_list[11]
    #     == 2
    # ):
    #     x = keypoints_list[3]
    #     y = keypoints_list[4]
    #     w = max(
    #         (keypoints_list[6] - keypoints_list[3]),
    #         (keypoints_list[9] - keypoints_list[0]),
    #     )
    #     h = max(
    #         (keypoints_list[4] - keypoints_list[1]),
    #         (keypoints_list[7] - keypoints_list[10]),
    #     )

    #     area = w * h

    # else:
    #     x = 0
    #     y = 0
    #     w = 0
    #     h = 0

    #     area = w * h

    #     return w, h, area

