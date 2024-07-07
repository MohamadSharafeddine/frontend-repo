import yaml

def read_config():
    with open("config.yaml", "r") as config_file:
        config_data = yaml.safe_load(config_file)
        global server_ip
        server_ip = config_data.get("ServerIPAddress")

read_config()
print(server_ip)

print("Check submodule update")