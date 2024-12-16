from utils.rc4 import rc4
from utils.wpa1 import wpa1

select_encryption = {
    "WEP": rc4,
    "WPA1": wpa1
}

def read_config(file_path,required_keys):
    config = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
    except FileNotFoundError:
        print("Configuration file not found. Please create 'wifi_config.txt'.")

    if not all(key in config for key in required_keys):
        print(f"{', '.join(required_keys)} not found in configuration file. Please update 'wifi_config.txt'.")
        return

    return config