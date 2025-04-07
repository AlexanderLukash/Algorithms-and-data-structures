import random
from dataclasses import dataclass


@dataclass
class GSLB:
    servers: list

    def get_best_server(self, client_region: str) -> dict:
        regional_servers = [s for s in self.servers if s['region'] == client_region]

        if not regional_servers:
            regional_servers = self.servers

        best_server = min(regional_servers, key=lambda s: s['latency'] + s['connections'])
        best_server['connections'] += 1
        return best_server


servers = [
    {'name': 'EU-1', 'region': 'Europe', 'latency': 20, 'connections': 0},
    {'name': 'EU-2', 'region': 'Europe', 'latency': 25, 'connections': 0},
    {'name': 'US-1', 'region': 'USA', 'latency': 50, 'connections': 0},
    {'name': 'ASIA-1', 'region': 'Asia', 'latency': 80, 'connections': 0},
]

gslb = GSLB(servers)


client_regions = ["Europe", "USA", "Asia", "Europe", "USA"]

for region in client_regions:
    server = gslb.get_best_server(region)
    print(f"Client from {region} -> Routed to: {server['name']}")

print("\nFinal server states:", servers)
