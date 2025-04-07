import random
from dataclasses import dataclass


@dataclass
class AntColonyLoadBalancer:
    servers: list
    alpha: int = 1
    evaporation_rate: float = 0.1

    def choose_server(self):
        total_pheromone = sum(server['pheromone'] for server in self.servers)

        probabilities = [
            (server, (server['pheromone'] / total_pheromone) ** self.alpha)
            for server in self.servers
        ]

        servers_list = [item[0] for item in probabilities]
        weights = [item[1] for item in probabilities]

        chosen_server = random.choices(servers_list, weights=weights, k=1)[0]
        chosen_server['pheromone'] += 1
        return chosen_server

    def evaporate_pheromones(self):
        for server in self.servers:
            server['pheromone'] *= (1 - self.evaporation_rate)


servers = [
    {
        "id": 1,
        "ip": "192.168.1.1",
        "port": 80,
        "weight": 5,
        "active_connections": 0,
        "response_time": 0,
        "time_remaining": 0,
        "location": "EU",
        "resource_usage": {"cpu": 50, "ram": 2048, "bandwidth": 100},
        "last_used": 1616161616,
        "failover_priority": 1,
        "hash_key": "abcd1234",
        "pheromone": 1.0
    },
    {
        "id": 2,
        "ip": "192.168.1.2",
        "port": 443,
        "weight": 3,
        "active_connections": 0,
        "response_time": 0,
        "time_remaining": 0,
        "location": "US",
        "resource_usage": {"cpu": 30, "ram": 1024, "bandwidth": 50},
        "last_used": 1616161620,
        "failover_priority": 2,
        "hash_key": "efgh5678",
        "pheromone": 1.0
    },
    {
        "id": 3,
        "ip": "192.168.1.3",
        "port": 8080,
        "weight": 2,
        "active_connections": 0,
        "response_time": 0,
        "time_remaining": 0,
        "location": "ASIA",
        "resource_usage": {"cpu": 70, "ram": 4096, "bandwidth": 200},
        "last_used": 1616161630,
        "failover_priority": 3,
        "hash_key": "ijkl91011",
        "pheromone": 1.0
    }
]

load_balancer = AntColonyLoadBalancer(servers)

for i in range(10):
    selected_server = load_balancer.choose_server()
    print(f"Request {i + 1} -> Routed to: {selected_server['id']}")
    load_balancer.evaporate_pheromones()

print("\nFinal pheromone levels:", load_balancer.servers)
