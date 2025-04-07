import random
from dataclasses import dataclass

@dataclass
class Server:
    name: str
    cpu_load: int
    ram_usage: int
    connections: int

    def available_capacity(self) -> int:
        return (100 - self.cpu_load) + (8000 - self.ram_usage) // 100 - self.connections

@dataclass
class ResourceLoadBalancer:
    servers: list

    def get_best_server(self) -> Server:
        best_server = max(self.servers, key=lambda s: s.available_capacity())
        best_server.connections += 1
        return best_server

servers = [
    Server(name="Server-1", cpu_load=random.randint(10, 20), ram_usage=random.randint(2000, 7000), connections=random.randint(0, 50)),
    Server(name="Server-2", cpu_load=random.randint(10, 20), ram_usage=random.randint(2000, 7000), connections=random.randint(0, 50)),
    Server(name="Server-3", cpu_load=random.randint(10, 20), ram_usage=random.randint(2000, 7000), connections=random.randint(0, 50)),
]

load_balancer = ResourceLoadBalancer(servers)

for _ in range(10):
    best_server = load_balancer.get_best_server()
    print(f"Request -> Routed to: {best_server.name} (CPU: {best_server.cpu_load}%, RAM: {best_server.ram_usage}MB, Connections: {best_server.connections})")

print("\nFinal server states:", servers)
