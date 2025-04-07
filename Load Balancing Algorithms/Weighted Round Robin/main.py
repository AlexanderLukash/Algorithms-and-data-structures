from dataclasses import dataclass


@dataclass
class WeightedRoundRobin:
    servers: list
    current_index: int = -1
    current_weight: int = 0

    def get_next_server(self):
        while True:
            self.current_index = (self.current_index + 1) % len(self.servers)
            if self.current_index == 0:
                self.current_weight -= 1
                if self.current_weight <= 0:
                    self.current_weight = max(self.servers, key=lambda server: server['weight'])['weight']
            if self.servers[self.current_index]['weight'] >= self.current_weight:
                return self.servers[self.current_index]


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
        'weight': 1,
        'connections': 0
    }
]
load_balancer = WeightedRoundRobin(servers)

for i in range(9):
    server = load_balancer.get_next_server()
    print(f"Request {i + 1} -> {server['name']}")
