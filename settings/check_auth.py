from json import load


def check(auth_file_path: str, key: str):

    # open the auth file
    with open(f'{auth_file_path}', 'r') as auth_file:

        # load the json file
        json_data = load(auth_file)

        # check if the entered key is in the list of valid keys
        if key in json_data.get('keys', []):

            # if yes, return True
            return True
    
    # return False by default (meaning that the above 'return True' wasn't already executed)
    return False



