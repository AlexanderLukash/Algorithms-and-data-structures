from dataclasses import dataclass


@dataclass
class WeightedRoundRobin:
    servers: list
    weights: list[int]
    current_index: int = -1
    current_weight: int = 0

    def get_next_server(self):
        while True:
            self.current_index = (self.current_index + 1) % len(self.servers)
            if self.current_index == 0:
                self.current_weight -= 1
                if self.current_weight <= 0:
                    self.current_weight = max(self.weights)
            if self.weights[self.current_index] >= self.current_weight:
                return self.servers[self.current_index]


servers = ["Server1", "Server2", "Server3"]
weights = [5, 1, 1]
load_balancer = WeightedRoundRobin(servers, weights)

for i in range(8):
    server = load_balancer.get_next_server()
    print(f"Request {i + 1} -> {server}")
