import random
from collections import deque
from dataclasses import dataclass, field


@dataclass
class LeastRecentlyUsed:
    servers: list

    def __post_init__(self, ):
        self.request_queue = deque(servers)  # Ініціалізація черги серверів

    def get_least_recently_used_server(self) -> dict:
        # Беремо сервер, який найменш недавно використовували (з початку черги)
        return self.request_queue.popleft()

    def route_request(self):
        selected_server = self.get_least_recently_used_server()
        selected_server['connections'] += 1  # Імітація додавання навантаження
        self.request_queue.append(selected_server)  # Додаємо сервер у кінець черги
        return selected_server


# Ініціалізація серверів
servers = [
    {'name': 'server1', 'connections': 0},
    {'name': 'server2', 'connections': 0},
    {'name': 'server3', 'connections': 0}
]

load_balancer = LeastRecentlyUsed(servers)

# Симуляція 10 запитів
for _ in range(10):
    selected_server = load_balancer.route_request()
    print(f'Request routed to: {selected_server["name"]}')
