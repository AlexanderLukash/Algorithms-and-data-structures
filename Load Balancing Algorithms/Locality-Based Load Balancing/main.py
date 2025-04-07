import random
from dataclasses import dataclass

@dataclass
class LocalityBasedLoadBalancer:
    servers: dict

    def get_nearest_servers(self, client_region: str) -> list:
        return self.servers.get(client_region, [])

    def route_request(self, client_region: str) -> dict:
        nearest_servers = self.get_nearest_servers(client_region)
        if not nearest_servers:
            return {"error": "No available servers for this region"}
        selected_server = random.choice(nearest_servers)
        selected_server['connections'] += 1
        return selected_server


servers = {
    "Europe": [{"name": "server1", "connections": 0}, {"name": "server2", "connections": 0}],
    "Asia": [{"name": "server3", "connections": 0}, {"name": "server4", "connections": 0}],
    "USA-East": [{"name": "server5", "connections": 0}, {"name": "server6", "connections": 0}],
}

load_balancer = LocalityBasedLoadBalancer(servers)

client_regions = ["Europe", "Asia", "USA-East", "Europe", "Asia"]

for region in client_regions:
    selected_server = load_balancer.route_request(region)
    print(f"Client from {region} -> Redirected to: {selected_server.get('name', 'No server')}")

print("\nFinal server states:", servers)
