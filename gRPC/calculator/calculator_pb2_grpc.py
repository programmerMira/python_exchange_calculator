# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculator.calculator_pb2 as calculator__pb2


class UnaryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AuthentificateUser = channel.unary_unary(
                '/unary.Unary/AuthentificateUser',
                request_serializer=calculator__pb2.User.SerializeToString,
                response_deserializer=calculator__pb2.UserResponse.FromString,
                )
        self.GetServerResponse = channel.unary_unary(
                '/unary.Unary/GetServerResponse',
                request_serializer=calculator__pb2.Message.SerializeToString,
                response_deserializer=calculator__pb2.MessageResponse.FromString,
                )


class UnaryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AuthentificateUser(self, request, context):
        """for authentification
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerResponse(self, request, context):
        """for calculations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UnaryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AuthentificateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthentificateUser,
                    request_deserializer=calculator__pb2.User.FromString,
                    response_serializer=calculator__pb2.UserResponse.SerializeToString,
            ),
            'GetServerResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerResponse,
                    request_deserializer=calculator__pb2.Message.FromString,
                    response_serializer=calculator__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'unary.Unary', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Unary(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AuthentificateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/AuthentificateUser',
            calculator__pb2.User.SerializeToString,
            calculator__pb2.UserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/unary.Unary/GetServerResponse',
            calculator__pb2.Message.SerializeToString,
            calculator__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
