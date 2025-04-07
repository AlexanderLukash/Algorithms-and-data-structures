import time
from dataclasses import dataclass, field
import random


@dataclass
class LeastResponseTime:
    servers: list

    def get_next_server(self):
        min_response_time = min(self.servers, key=lambda server: server['response_time'])
        return min_response_time

    def update_response_time(self, server, response_time):
        server['response_time'] = response_time


def simulate_response_time():
    # Simulating response time with random delay
    delay = random.uniform(0.1, 1.0)

    return delay


# Example usage
servers = [
    {
        'name': 'Server1',
        'response_time': 0,
        'connections': 0
    },
    {
        'name': 'Server2',
        'response_time': 0,
        'connections': 0
    },
    {
        'name': 'Server3',
        'response_time': 0,
        'connections': 0
    }
]

load_balancer = LeastResponseTime(servers)

for i in range(10):
    server = load_balancer.get_next_server()
    print(f"Request {i + 1} -> {server['name']}")
    response_time = simulate_response_time()
    load_balancer.update_response_time(server, response_time)
    print(f"Response Time: {response_time:.2f}s")
