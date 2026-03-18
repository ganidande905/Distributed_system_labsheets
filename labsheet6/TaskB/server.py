from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.num1 + request.num2
        return calculator_pb2.CalcReply(result=result, message="Addition successful")

    def Subtract(self, request, context):
        result = request.num1 - request.num2
        return calculator_pb2.CalcReply(result=result, message="Subtraction successful")

    def Multiply(self, request, context):
        result = request.num1 * request.num2
        return calculator_pb2.CalcReply(result=result, message="Multiplication successful")

    def Divide(self, request, context):
        if request.num2 == 0:
            return calculator_pb2.CalcReply(result=0, message="Error: Division by zero is not allowed")
        result = request.num1 / request.num2
        return calculator_pb2.CalcReply(result=result, message="Division successful")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("Task B Calculator gRPC server running on port 50052...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()