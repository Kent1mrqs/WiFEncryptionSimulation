def xor_encrypt_decrypt(message, key):
    key = str(key)
    encrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, key * len(message)))
    return encrypted

def read_config(file_path):
    """Read the Wi-Fi configuration from a file."""
    config = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config[key] = value
    except FileNotFoundError:
        print("Configuration file not found. Please create 'wifi_config.txt'.")
    return config


def connect_to_wifi(ssid):
    """Simulate connecting to an open Wi-Fi network."""
    print(f"Attempting to connect to Wi-Fi network: {ssid}")
    print(f"Connected to {ssid}. No password required.")


def simulate_wifi_connection():
    """Main function to simulate Wi-Fi connection."""
    # Step 1: Read the configuration file
    config = read_config("wifi_config.txt")

    # Step 2: Check if SSID is provided
    if 'SSID' not in config:
        print("SSID not found in configuration file. Please update 'wifi_config.txt'.")
        return

    # Step 3: Simulate connecting to the Wi-Fi network
    ssid = config['SSID']
    connect_to_wifi(ssid)