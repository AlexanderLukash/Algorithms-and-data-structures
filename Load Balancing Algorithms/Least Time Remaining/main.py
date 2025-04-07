import random
from dataclasses import dataclass


@dataclass
class LeastTimeRemaining:
    servers: list

    def assist_task(self, task_time):
        best_server = min(self.servers, key=lambda server: server['remaining_time'])
        return best_server

    def route_request(self, task):
        selected_server = self.assist_task(task)
        selected_server['remaining_time'] += task
        return selected_server

servers = [
    {'name': 'server1', 'remaining_time': 0},
    {'name': 'server2', 'remaining_time': 0},
    {'name': 'server3', 'remaining_time': 0}
]
load_balancer = LeastTimeRemaining(servers)

tasks = [random.randint(1, 10) for _ in range(10)]


for task in tasks:
    select_server = load_balancer.route_request(task)
    print(f'Request: {select_server['name']}')