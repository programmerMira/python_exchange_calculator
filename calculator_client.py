import grpc
import calculator.calculator_pb2_grpc as pb2_grpc
import calculator.calculator_pb2 as pb2


class CalculatorClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def auth(self, login, password):
        """
        Client function to call the rpc for AuthentificateUser
        """
        user = pb2.User(login=login, password=password)
        return self.stub.AuthentificateUser(user)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = CalculatorClient()
    message = ""
    result = client.auth("user1", "qwerty")
    print(f'{result}')
    while(True):
        print("Enter expression:")
        message = input()
        if(message.lower()=="q"):
            print("Bye!")
            break
        result = client.get_url(message=message)
        print("Server reply")
        print(f'{result}')