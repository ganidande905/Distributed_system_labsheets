import grpc
import calculator_pb2
import calculator_pb2_grpc


def menu():
    print("\n===== MENU DRIVEN CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def run():
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        while True:
            menu()
            choice = input("Enter your choice: ")

            if choice == "5":
                print("Exiting calculator client...")
                break

            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice. Please try again.")
                continue

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            request = calculator_pb2.CalcRequest(num1=num1, num2=num2)

            if choice == "1":
                response = stub.Add(request)
            elif choice == "2":
                response = stub.Subtract(request)
            elif choice == "3":
                response = stub.Multiply(request)
            elif choice == "4":
                response = stub.Divide(request)

            print("Message:", response.message)
            print("Result:", response.result)


if __name__ == "__main__":
    run()