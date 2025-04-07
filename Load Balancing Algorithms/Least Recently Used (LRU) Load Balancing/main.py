import random
from dataclasses import dataclass, field
from collections import deque

@dataclass
class LRU_LoadBalancer:
    servers: list
    history: deque = field(default_factory=lambda: deque(maxlen=5))

    def assist_task(self):
        least_used_server = min(self.servers, key=lambda server: self.history.count(server['name']))
        return least_used_server

    def route_request(self, task):
        selected_server = self.assist_task()
        self.history.append(selected_server['name'])
        selected_server['task_count'] += 1
        return selected_server


servers = [
    {'name': 'server1', 'task_count': 0},
    {'name': 'server2', 'task_count': 0},
    {'name': 'server3', 'task_count': 0}
]

load_balancer = LRU_LoadBalancer(servers)


tasks = [random.randint(1, 10) for _ in range(10)]


for task in tasks:
    selected_server = load_balancer.route_request(task)
    print(f'Request routed to: {selected_server["name"]}')