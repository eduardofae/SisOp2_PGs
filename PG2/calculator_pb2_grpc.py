# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculator_pb2 as calculator__pb2


class CalculatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sum = channel.unary_unary(
                '/Calculator/Sum',
                request_serializer=calculator__pb2.SumRequest.SerializeToString,
                response_deserializer=calculator__pb2.SumReply.FromString,
                )
        self.Multiply = channel.unary_unary(
                '/Calculator/Multiply',
                request_serializer=calculator__pb2.MultiplyRequest.SerializeToString,
                response_deserializer=calculator__pb2.MultiplyReply.FromString,
                )
        self.Max = channel.unary_unary(
                '/Calculator/Max',
                request_serializer=calculator__pb2.MaxRequest.SerializeToString,
                response_deserializer=calculator__pb2.MaxReply.FromString,
                )
        self.Division = channel.unary_unary(
                '/Calculator/Division',
                request_serializer=calculator__pb2.DivisionRequest.SerializeToString,
                response_deserializer=calculator__pb2.DivisionReply.FromString,
                )


class CalculatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Sum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Multiply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Max(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Division(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Sum': grpc.unary_unary_rpc_method_handler(
                    servicer.Sum,
                    request_deserializer=calculator__pb2.SumRequest.FromString,
                    response_serializer=calculator__pb2.SumReply.SerializeToString,
            ),
            'Multiply': grpc.unary_unary_rpc_method_handler(
                    servicer.Multiply,
                    request_deserializer=calculator__pb2.MultiplyRequest.FromString,
                    response_serializer=calculator__pb2.MultiplyReply.SerializeToString,
            ),
            'Max': grpc.unary_unary_rpc_method_handler(
                    servicer.Max,
                    request_deserializer=calculator__pb2.MaxRequest.FromString,
                    response_serializer=calculator__pb2.MaxReply.SerializeToString,
            ),
            'Division': grpc.unary_unary_rpc_method_handler(
                    servicer.Division,
                    request_deserializer=calculator__pb2.DivisionRequest.FromString,
                    response_serializer=calculator__pb2.DivisionReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Sum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculator/Sum',
            calculator__pb2.SumRequest.SerializeToString,
            calculator__pb2.SumReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Multiply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculator/Multiply',
            calculator__pb2.MultiplyRequest.SerializeToString,
            calculator__pb2.MultiplyReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Max(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculator/Max',
            calculator__pb2.MaxRequest.SerializeToString,
            calculator__pb2.MaxReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Division(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Calculator/Division',
            calculator__pb2.DivisionRequest.SerializeToString,
            calculator__pb2.DivisionReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
