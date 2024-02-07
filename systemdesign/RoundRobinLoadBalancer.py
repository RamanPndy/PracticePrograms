class RoundRobinLoadBalancer:
    '''
    
    '''
    def __init__(self, servers=None):
        self.servers = servers or []
        self.current_index = 0

    def add_server(self, server):
        self.servers.append(server)

    def remove_server(self, server):
        if server in self.servers:
            self.servers.remove(server)

    def route_request(self):
        if not self.servers:
            return None

        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server
    
    def next_server(self):
        if not self.servers:
            return None
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

# Example usage
if __name__ == "__main__":
    # Create load balancer
    lb = RoundRobinLoadBalancer()

    # Add servers
    lb.add_server("Server 1")
    lb.add_server("Server 2")
    lb.add_server("Server 3")

    # Route requests
    for _ in range(5):
        server = lb.route_request()
        if server:
            print("Routing request to:", server)
        else:
            print("No servers available.")
