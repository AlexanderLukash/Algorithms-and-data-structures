import random
from dataclasses import dataclass


@dataclass
class ChainedFailoverBalancer:
    servers: list

    def check_server(self):
        return random.random() < 0.8


    def route_request(self):
        for server in self.servers:
            if self.check_server():
                server['connections'] += 1
                return server

        return 'Error'


servers = [
    {'name': 'server1', 'connections': 0},
    {'name': 'server2', 'connections': 0},
    {'name': 'server3', 'connections': 0}
]

load_balancer = ChainedFailoverBalancer(servers)

for _ in range(10):
    selected_server = load_balancer.route_request()
    print(f"Request -> Redirected to: {selected_server.get('name', 'No server')}")

print("\nFinal server states:", servers)