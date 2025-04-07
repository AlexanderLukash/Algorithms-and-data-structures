from dataclasses import dataclass
import hashlib


@dataclass
class URLHash:
    servers: list

    def get_next_server(self, url):
        hash_value = hashlib.md5(url.encode()).hexdigest()
        index = int(hash_value, 16) % len(self.servers)
        return self.servers[index]


servers = ["Server1", "Server2", "Server3"]
load_balancer = URLHash(servers)

urls = [
    "/home",
    "/about",
    "/home",
    "/products/item1",
    "/contact",
    "/products/item1"
]

for url in urls:
    server = load_balancer.get_next_server(url)
    print(f"URL {url} -> {server}")
