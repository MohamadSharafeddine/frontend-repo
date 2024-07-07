import yaml

class Client:
    def __init__(self, config_path='\config.yaml'):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.server_ip = self.config['ServerIPAddress']

    def run(self):
        print(f'Client connecting to server at {self.server_ip}')

if __name__ == "__main__":
    client = Client()
    client.run()