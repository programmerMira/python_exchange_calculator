import grpc
from concurrent import futures
import time
import calculator.calculator_pb2_grpc as pb2_grpc
import calculator.calculator_pb2 as pb2


class CalculatorService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        calculated = str(eval(message,{},{}))
        result = f'Recieved expression: {message} = {calculated}'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(CalculatorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port [::]:50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()