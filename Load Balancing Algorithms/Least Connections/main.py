import random
from dataclasses import dataclass


@dataclass
class LeastConnections:
    servers: list

    def get_least_connections_server(self):
        min_connections = min(self.servers, key=lambda server: server['connections'])
        return min_connections

    def route_request(self):
        selected_server = self.get_least_connections_server()
        selected_server['connections'] += 1
        return selected_server


servers = [{'name': 'server1', 'connections': 0},
           {'name': 'server2', 'connections': 0},
           {'name': 'server3', 'connections': 0}]

load_balancer = LeastConnections(servers)

for _ in range(10):
    selected_server = load_balancer.route_request()
    print("The request is aimed at the server:", selected_server['name'])


@dataclass
class LeastConnectionsRandom(LeastConnections):

    def get_least_loaded_servers(self):
        # Get the minimum number of connections
        min_connections = self.get_least_connections_server()['connections']
        # Return all servers with the minimum number of connections
        return [server for server in self.servers
                if server['connections'] == min_connections]

    def route_request(self):
        least_loaded_servers = self.get_least_loaded_servers()
        selected_server = random.choice(least_loaded_servers)
        selected_server['connections'] += 1
        return selected_server


servers = [{'name': 'server1', 'connections': 0},
           {'name': 'server2', 'connections': 0},
           {'name': 'server3', 'connections': 0}]

load_balancer = LeastConnectionsRandom(servers)
print('_' * 25)
for _ in range(10):
    print(servers)
    selected_server = load_balancer.route_request()
    print("The request is aimed at the server:", selected_server['name'])
