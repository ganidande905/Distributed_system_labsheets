import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)

        name = input("Enter your name: ")

        response1 = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
        print("SayHello Response:", response1.message)

        response2 = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name=name))
        print("SayHelloAgain Response:", response2.message)


if __name__ == "__main__":
    run()