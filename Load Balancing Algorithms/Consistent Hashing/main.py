from dataclasses import dataclass, field
import hashlib
import bisect


@dataclass
class ConsistentHash:
    replicas: int = 3
    sorted_keys: list = field(default_factory=list)
    ring: dict = field(default_factory=dict)

    @staticmethod
    def _hash(key):
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


servers = ["Server1", "Server2", "Server3"]
load_balancer = ConsistentHash(replicas=3)
load_balancer.add_server(servers[0])
load_balancer.add_server(servers[1])
load_balancer.add_server(servers[2])

client_ips = ["192.168.2.1", "192.168.0.2", "192.168.0.1", "192.168.0.34", "192.168.0.4", "192.168.0.34"]
for ips in client_ips:
    server = load_balancer.get_server(ips)
    print(f"Client {ips} -> {server}")

load_balancer.remove_server(servers[1])

print('\n\n')
for ips in client_ips:
    server = load_balancer.get_server(ips)
    print(f"Client {ips} -> {server}")
