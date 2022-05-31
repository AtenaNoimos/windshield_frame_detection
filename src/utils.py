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

