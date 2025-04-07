import random
from dataclasses import dataclass


@dataclass
class SlowestResponseTime:
    servers: list

    def get_slowest_server(self):
        slowest_server = max(self.servers, key=lambda server: server['response_time'])
        return slowest_server

    def route_request(self):
        selected_server = self.get_slowest_server()
        selected_server['response_time'] = random.uniform(0.1, 0.5)
        return selected_server


servers = [
    {'name': 'server1', 'response_time': random.uniform(0.1, 0.5)},
    {'name': 'server2', 'response_time': random.uniform(0.1, 0.5)},
    {'name': 'server3', 'response_time': random.uniform(0.1, 0.5)}
]
load_balancer = SlowestResponseTime(servers)

for i in range(30):
    select_server = load_balancer.route_request()
    print(f'Request: {select_server['name']}')
