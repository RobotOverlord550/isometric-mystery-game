import json


#TODO: (not urgent) at some point should also add a function to write a dict to a json file for saving game data
def get_json_dict(path) -> dict:
    """get python dictionary from json data

    Args:
        path (sys.path ot str): path to json file

    Returns:
        dict: python disctionary of json file
    """    
    with open(path, 'r') as file:
        data = json.load(file)
        return data
