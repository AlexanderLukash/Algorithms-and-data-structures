import bisect
import hashlib
import random

from dataclasses import dataclass, field

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
        "pheromone": 1.0  # Початкове значення феромону
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


@dataclass
class LeastConnection:
    servers: list

    def get_least_connections_server(self):
        min_connection = min(self.servers, key=lambda server: server['active_connections'])
        return min_connection

    def route_request(self):
        selected_server = self.get_least_connections_server()
        selected_server['active_connections'] += 1
        return selected_server


print(f'\n{'-' * 8} Least Connections {'-' * 8}')
lb = LeastConnection(servers)
for i in range(10):
    server = lb.route_request()
    print(f'Request to {server['id']}')


@dataclass
class WeightedRoundRobin:
    servers: list
    _index: int = 0
    _current_weight: int = 0

    def route_request(self):
        while True:
            server = self.servers[self._index]
            if self._current_weight < server['weight']:
                self._current_weight += 1
                return server
            self._current_weight = 0
            self._index = (self._index + 1) % len(servers)


print(f'\n{'-' * 8} Weight Round Robin {'-' * 8}')
lb = WeightedRoundRobin(servers)
for i in range(10):
    server = lb.route_request()
    print(f'Request to {server['id']}')


@dataclass
class WeightLeastConnections:
    servers: list

    def get_weight_least_connections_server(self):
        best_server = min(self.servers, key=lambda server: server['active_connections'] / server['weight'])
        return best_server

    def route_request(self):
        selected_server = self.get_weight_least_connections_server()
        selected_server['active_connections'] += 1
        return selected_server


print(f'\n{'-' * 8} Weight Least Connections {'-' * 8}')
lb = WeightLeastConnections(servers)
for i in range(10):
    server = lb.route_request()
    print(f'Request to {server['id']}')


@dataclass
class LeastResponseTime:
    servers: list

    def simulate_response_time(self):
        response_time = random.randint(50, 300)
        return response_time

    def get_best_server(self):
        best_server = min(self.servers, key=lambda server: server['response_time'])
        return best_server

    def route_request(self):
        selected_server = self.get_best_server()
        selected_server['response_time'] = self.simulate_response_time()
        return selected_server


print(f'\n{'-' * 8} Least Response Time {'-' * 8}')
lb = LeastResponseTime(servers)
for i in range(10):
    server = lb.route_request()
    print(f'Request to {server['id']}')


@dataclass
class LeastTimeRemaining:
    servers: list

    def get_best_server(self):
        best_server = min(self.servers, key=lambda server: server["time_remaining"])
        return best_server

    def route_request(self, task):
        selected_server = self.get_best_server()
        selected_server['time_remaining'] += task
        return selected_server


print(f'\n{'-' * 8} Least Time Remaining {'-' * 8}')
lb = LeastTimeRemaining(servers)
tasks = [random.randint(1, 10) for _ in range(10)]
for task in tasks:
    server = lb.route_request(task)
    print(f'Request to {server['id']}')


@dataclass
class IPHash:
    servers: list

    def route_request(self, ip):
        hash_key = int(hashlib.md5(ip.encode()).hexdigest(), 16)
        index = hash_key % len(self.servers)
        return self.servers[index]


print(f'\n{'-' * 8} IP Hash {'-' * 8}')
lb = IPHash(servers)
client_ips = ["192.168.2123.1", "192.168.0.2", "192.168.0.1", "192.168.0.34", "192.168.0.4", "192.168.0.34"]
for ip in client_ips:
    server = lb.route_request(ip)
    print(f'Request to {server['id']}')


@dataclass
class URLHash:
    servers: list

    def route_request(self, url):
        hash_key = int(hashlib.md5(url.encode()).hexdigest(), 16)
        index = hash_key % len(self.servers)
        return self.servers[index]


print(f'\n{'-' * 8} URL Hash {'-' * 8}')
lb = URLHash(servers)
urls = [
    "/home",
    "/about",
    "/home",
    "/products/item1",
    "/contact",
    "/products/item1"
]
for url in urls:
    server = lb.route_request(url)
    print(f'Request to {server['id']}')


@dataclass
class ConsistentHashing:
    replicas: int = 3
    ring: dict = field(default_factory=dict)
    sorted_keys: list = field(default_factory=list)

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_server(self, server):
        for i in range(self.replicas):
            key = self._hash(f'{server}-{i}')
            self.ring[key] = server
            bisect.insort(self.sorted_keys, key)

    def remove_server(self, server):
        for i in range(self.replicas):
            key = self._hash(f'{server}-{i}')
            if key in self.ring:
                del self.ring[key]
                self.sorted_keys.remove(key)

    def get_server(self, key):
        hash_key = self._hash(key)
        index = bisect.bisect(self.sorted_keys, hash_key) % len(self.sorted_keys)
        return self.ring[self.sorted_keys[index]]


print(f'\n{'-' * 8} Consistent Hashing {'-' * 8}')
lb = ConsistentHashing(replicas=3)
lb.add_server(servers[0])
lb.add_server(servers[1])
lb.add_server(servers[2])

for i in range(10):
    server = lb.get_server(f'{i + 23343}')
    print(f'Request to {server['id']}')


@dataclass
class RandomWithRetry:
    servers: list
    retries: int = 3

    def check_server_avaible(self):
        return random.random() < 0.8

    def route_request(self):
        for i in range(self.retries):
            selected_server = random.choice(self.servers)

            if self.check_server_avaible():
                return selected_server
            else:
                raise Exception("All retries failed, no available servers")


print(f'\n{'-' * 8} Random with Retry {'-' * 8}')
lb = RandomWithRetry(servers)
for i in range(10):
    try:
        select_server = lb.route_request()
        print(f'Request: {select_server['id']}')
    except Exception as error:
        print(error)


@dataclass
class FastestResponseTime:
    servers: list

    def get_best_server(self):
        for server in self.servers:
            server['response_time'] = random.randint(50, 300)

        best_server = min(self.servers, key=lambda server: server['response_time'])
        return best_server


print(f'\n{'-' * 8} Fastest Response Time {'-' * 8}')
lb = FastestResponseTime(servers)
for i in range(10):
    select_server = lb.get_best_server()
    print(f'Request: {select_server['id']}')


@dataclass
class SlowestResponseTime:
    servers: list

    def get_best_server(self):
        for server in self.servers:
            server['response_time'] = random.randint(50, 300)

        best_server = max(self.servers, key=lambda server: server['response_time'])
        return best_server


print(f'\n{'-' * 8} Slowest Response Time {'-' * 8}')
lb = SlowestResponseTime(servers)
for i in range(10):
    select_server = lb.get_best_server()
    print(f'Request: {select_server['id']}')


@dataclass
class LocalityBasedLoadBalancing:
    servers: list

    def get_best_server(self, client_geo):
        for server in servers:
            if server['location'] == client_geo:
                return server

        return min(self.servers, key=lambda server: server['response_time'])


print(f'\n{'-' * 8} Locality-Based Load Balancing {'-' * 8}')
lb = LocalityBasedLoadBalancing(servers)
client_regions = ["EU", "ASIA", "US", "EU", "ASIA", "US"]
for client_geo in client_regions:
    server = lb.get_best_server(client_geo)
    print(f'Request: {server['id']}')

@dataclass
class ChainedFailover:
    servers: list

    def check_server_available(self):
        return random.random() < 0.8

    def route_request(self):
        sorted_server = sorted(self.servers, key=lambda server: server['failover_priority'])

        for server in sorted_server:
            if self.check_server_available():
                return server

print(f'\n{'-' * 8} ChainedFailover {'-' * 8}')
lb = ChainedFailover(servers)
for i in range(10):
    select_server = lb.route_request()
    print(f'Request: {select_server['id']}')


@dataclass
class GSLB:
    servers: list

    def route_request(self, client_geo):
        regional_servers = [server for server in self.servers if server['location'] == client_geo]

        if not regional_servers:
            regional_servers = self.servers

        best_server = min(regional_servers, key=lambda server: server['response_time'] + server['active_connections'])
        best_server['active_connections'] += 1
        return best_server

print(f'\n{'-' * 8} GSLB {'-' * 8}')
lb = GSLB(servers)
client_regions = ["EU", "ASIA", "US", "EU", "ASIA", "US"]
for client_geo in client_regions:
    server = lb.route_request(client_geo)
    print(f'Request: {server['id']}')

