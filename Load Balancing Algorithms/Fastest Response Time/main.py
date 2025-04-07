import random
from dataclasses import dataclass


@dataclass
class FastestResponseTime:
    servers: list

    def get_fastest_server(self):
        fastest_server = min(self.servers, key=lambda server: server['avg_response_time'])
        return fastest_server

    def route_request(self):
        selected_server = self.get_fastest_server()
        current_response_time = random.uniform(0.1, 0.5)
        selected_server['avg_response_time'] = (
                selected_server['avg_response_time'] * 0.9 + current_response_time * 0.1
        )
        selected_server['requests'] += 1
        return selected_server


servers = [
    {'name': 'server1', 'avg_response_time': 0, 'requests': 0},
    {'name': 'server2', 'avg_response_time': 0, 'requests': 0},
    {'name': 'server3', 'avg_response_time': 0, 'requests': 0}
]

load_balancer = FastestResponseTime(servers)

for _ in range(10):
    selected_server = load_balancer.route_request()
    print(f"Запит спрямований на сервер: {selected_server['name']}, "
          f"середній час відповіді: {selected_server['avg_response_time']:.3f} сек")
