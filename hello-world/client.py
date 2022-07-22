import grpc
import greeting_pb2
import greeting_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel)
        for _ in range(10000):
            response=stub.greet(greeting_pb2.ClientInput(name="Fanta", greeting='Hello,'))
            print("Received from the server: "+response.message)

run()