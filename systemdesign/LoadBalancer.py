class Server:
    def __init__(self, server_id, ip_address):
        self.server_id = server_id
        self.ip_address = ip_address

class LoadBalancer:
    def __init__(self):
        self.servers = []

    def add_server(self, ip_address):
        server_id = len(self.servers) + 1
        server = Server(server_id, ip_address)
        self.servers.append(server)

    def remove_server(self, server_id):
        self.servers = [server for server in self.servers if server.server_id != server_id]

    def get_next_server(self):
        if not self.servers:
            return None
        return self.servers[0]

    def route_request(self):
        next_server = self.get_next_server()
        if next_server:
            print(f"Routing request to Server {next_server.server_id} at {next_server.ip_address}")
            self.servers.append(self.servers.pop(0))  # Move the first server to the end for round-robin
        else:
            print("No servers available.")

# Example usage
if __name__ == "__main__":
    load_balancer = LoadBalancer()

    # Add servers
    load_balancer.add_server("192.168.1.1")
    load_balancer.add_server("192.168.1.2")
    load_balancer.add_server("192.168.1.3")

    # Route requests
    for _ in range(5):
        load_balancer.route_request()
