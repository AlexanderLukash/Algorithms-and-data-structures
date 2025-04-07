import random
from dataclasses import dataclass


@dataclass
class PriorityLoadBalancer:
    servers: list  # Список серверів із пріоритетами

    def check_server(self, server: dict) -> bool:
        return random.random() < 0.8

    def get_server(self) -> dict:
        sorted_servers = sorted(self.servers, key=lambda s: s['priority'])

        for server in sorted_servers:
            if self.check_server(server):
                server['connections'] += 1
                return server
        return {"error": "No available servers"}


servers = [
    {'name': 'server1', 'priority': 1, 'connections': 0},
    {'name': 'server2', 'priority': 2, 'connections': 0},
    {'name': 'server3', 'priority': 3, 'connections': 0}
]

load_balancer = PriorityLoadBalancer(servers)

# Тестуємо балансувальник
for _ in range(10):
    selected_server = load_balancer.get_server()
    print(f"Request -> Routed to: {selected_server.get('name', 'No server available')}")

print("\nFinal server states:", servers)
