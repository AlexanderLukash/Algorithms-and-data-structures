import random
from dataclasses import dataclass


@dataclass
class RandomWithRetry:
    servers: list
    max_retries: int

    def route_request(self):
        for _ in range(self.max_retries):
            selected_server = random.choice(self.servers)

            if self.is_server_available():
                return selected_server
            else:
                raise Exception("All retries failed, no available servers")

    @staticmethod
    def is_server_available():
        return random.random() < 0.8

servers = [
    {'name': 'server1', 'remaining_time': 0},
    {'name': 'server2', 'remaining_time': 0},
    {'name': 'server3', 'remaining_time': 0}
]
load_balancer = RandomWithRetry(servers, 3)

for i in range(11):
    try:
        select_server = load_balancer.route_request()
        print(f'Request: {select_server['name']}')
    except Exception as error:
        print(error)