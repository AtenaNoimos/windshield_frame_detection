import json


def read_json(json_file_path):
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

