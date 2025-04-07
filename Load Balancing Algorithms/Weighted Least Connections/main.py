from dataclasses import dataclass


@dataclass
class WeightLeastConnections:
    servers: list

    def get_least_weight_connections_server(self):
        min_connections = min(self.servers, key=lambda server: server['connections'] / server['weight'])
        return min_connections

    def route_request(self):
        selected_server = self.get_least_weight_connections_server()
        selected_server['connections'] += 1
        return selected_server


servers = [
    {
        'name': 'Server1',
        'weight': 5,
        'connections': 0
    },
    {
        'name': 'Server2',
        'weight': 3,
        'connections': 0
    },
    {
        'name': 'Server3',
        'weight': 2,
        'connections': 0
    }
]

load_balancer = WeightLeastConnections(servers)

for i in range(10):
    select = load_balancer.route_request()
    print(f'Request to {select['name']}')
