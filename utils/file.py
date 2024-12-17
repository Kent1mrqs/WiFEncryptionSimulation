from utils.rc4 import rc4
import time

select_encryption = {
    "WEP": rc4
}

def generate_iv():
    current_time = int(time.time() * 1000000)
    iv = current_time & 0xFFFFFF

    iv_str = iv.to_bytes(3, byteorder='big')
    return iv_str

def read_config(file_path,required_keys):
    config = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
    except FileNotFoundError:
        print("Configuration file not found. Please create configuration file (client_config.txt/server_config.txt).")

    if not all(key in config for key in required_keys):
        print(f"{', '.join(required_keys)} not found in configuration file. Please update configuration file (server_config.txt/client_config.txt).")
        return

    return config