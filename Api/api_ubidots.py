import requests

TOKEN = "BBFF-yxwyI0o8XzN8YMLoDflTqQbm2AtwYk" # Assign your Ubidots Token
DEVICE = "10521c01f52f" # Assign the device label to obtain the variable
VARIABLE_1 = "mesa-1" # Assign the variable label to obtain the variable value
VARIABLE_2 = "mesa-2"
DELAY = 1  # Delay in seconds

def get_var(device, variable):
    try:
        url = "http://industrial.api.ubidots.com/"
        url = url + \
            "api/v1.6/devices/{0}/{1}/".format(device, variable)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        req = requests.get(url=url, headers=headers)
        return req.json()['last_value']['value']
    except:
        pass


def spaces_status():
    spaces = {
        "M1" : get_var(DEVICE, VARIABLE_1),
        "M2" :  get_var(DEVICE, VARIABLE_2)
    }
    return spaces


    