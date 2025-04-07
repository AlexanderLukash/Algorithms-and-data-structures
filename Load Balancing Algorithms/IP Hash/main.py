import hashlib
from dataclasses import dataclass


@dataclass
class IPHash:
    servers: list

    def get_next_server(self, client_ip):
        hash_value = int(hashlib.md5(client_ip.encode()).hexdigest(), 16)
        index = hash_value % len(self.servers)
        return self.servers[index]

servers = ["Server1", "Server2", "Server3"]
load_balancer = IPHash(servers)

client_ips = ["192.168.2123.1", "192.168.0.2", "192.168.0.1", "192.168.0.34", "192.168.0.4", "192.168.0.34"]
for ip in client_ips:
    server = load_balancer.get_next_server(ip)
    print(f"Client {ip} -> {server}")