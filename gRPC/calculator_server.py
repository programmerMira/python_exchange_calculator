import grpc
from concurrent import futures
import time
import calculator.calculator_pb2_grpc as pb2_grpc
import calculator.calculator_pb2 as pb2
from users import USERS

class CalculatorService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        LOGGED_IN = False
    
    def AuthentificateUser(self, request, context):
        # get the string from the incoming request
        login = request.login
        password = request.password
        try:
            if login in USERS and USERS[login]==password:
                result = {'message': "Logged in!", 'logged_in': True}
                self.LOGGED_IN = True
            else:
                result = {'message': "Bad cridentials!", 'logged_in': False}
                self.LOGGED_IN = False
        except Exception as e:
            result = f'Recieved expression but error occured: {e}'
            result = {'message': result, 'logged_in': False}
        finally:
            return pb2.UserResponse(**result)

    def GetServerResponse(self, request, context):
        if self.LOGGED_IN:
            # get the string from the incoming request
            message = request.message
            try:
                calculated = str(eval(message,{},{}))
                result = f'Recieved expression: {message} = {calculated}'
                result = {'message': result, 'received': True}
            except Exception as e:
                result = f'Recieved expression but error occured: {e}'
                result = {'message': result, 'received': True}
            finally:
                return pb2.MessageResponse(**result)
        else:
            result = {'message': "Auth error", 'received': False}
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