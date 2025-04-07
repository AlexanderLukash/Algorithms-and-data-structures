import time
import random
from dataclasses import dataclass


@dataclass
class ThrottleLoadBalancer:
    servers: list
    rate_limit: int
    time_window: int
    requests_log: dict = None

    def __post_init__(self):

        self.requests_log = {server: [] for server in self.servers}

    def throttle_check(self, server: str) -> bool:

        current_time = time.time()

        self.requests_log[server] = [t for t in self.requests_log[server] if current_time - t < self.time_window]


        if len(self.requests_log[server]) < self.rate_limit:
            return True
        return False

    def route_request(self):
        random.shuffle(self.servers)
        for server in self.servers:
            if self.throttle_check(server):
                self.requests_log[server].append(time.time())
                return f"Request routed to {server}"

        return "All servers are throttled, try again later."


# Список серверів
servers = ["Server-1", "Server-2", "Server-3"]


load_balancer = ThrottleLoadBalancer(servers=servers, rate_limit=5, time_window=60)


for _ in range(20):
    result = load_balancer.route_request()
    print(result)

