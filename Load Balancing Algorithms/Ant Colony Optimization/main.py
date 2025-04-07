import random

class AntColonyLoadBalancer:
    def __init__(self, servers, alpha=1, evaporation_rate=0.1):
        self.servers = {server: 1.0 for server in servers}
        self.alpha = alpha
        self.evaporation_rate = evaporation_rate

    def choose_server(self):
        total_pheromone = sum(self.servers.values())
        probabilities = {server: (pheromone / total_pheromone) ** self.alpha for server, pheromone in self.servers.items()}
        chosen_server = random.choices(list(probabilities.keys()), weights=probabilities.values(), k=1)[0]

        self.servers[chosen_server] += 1
        return chosen_server

    def evaporate_pheromones(self):
        for server in self.servers:
            self.servers[server] *= (1 - self.evaporation_rate)


servers = ["Server-1", "Server-2", "Server-3"]
load_balancer = AntColonyLoadBalancer(servers)


for i in range(10):
    selected_server = load_balancer.choose_server()
    print(f"Request {i+1} -> Routed to: {selected_server}")
    load_balancer.evaporate_pheromones()

print("\nFinal pheromone levels:", load_balancer.servers)
