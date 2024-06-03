import grpc
import example_pb2
import example_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.ExampleServiceStub(channel)
        response_stream = stub.GetServerStream(example_pb2.Request())
        for response in response_stream:
            print(response.message)

if __name__ == '__main__':
    run()
