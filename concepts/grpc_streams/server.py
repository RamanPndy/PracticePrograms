import grpc
from concurrent import futures
import time
import example_pb2
import example_pb2_grpc

class ExampleService(example_pb2_grpc.ExampleServiceServicer):
    def GetServerStream(self, request, context):
        for i in range(5):
            response = example_pb2.Response(message=f"Message {i}")
            yield response
            time.sleep(1)  # Simulate delay

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
