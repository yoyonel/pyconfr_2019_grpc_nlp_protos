# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pyconfr_2019.grpc_nlp.protos import StorageService_pb2 as pyconfr__2019_dot_grpc__nlp_dot_protos_dot_StorageService__pb2


class StorageServiceStub(object):
  """API
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StoreTweetsStream = channel.stream_unary(
        '/pyconfr_2019.grpc_nlp.StorageService/StoreTweetsStream',
        request_serializer=pyconfr__2019_dot_grpc__nlp_dot_protos_dot_StorageService__pb2.StoreTweetsRequest.SerializeToString,
        response_deserializer=pyconfr__2019_dot_grpc__nlp_dot_protos_dot_StorageService__pb2.StoreTweetsResponse.FromString,
        )


class StorageServiceServicer(object):
  """API
  """

  def StoreTweetsStream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StorageServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StoreTweetsStream': grpc.stream_unary_rpc_method_handler(
          servicer.StoreTweetsStream,
          request_deserializer=pyconfr__2019_dot_grpc__nlp_dot_protos_dot_StorageService__pb2.StoreTweetsRequest.FromString,
          response_serializer=pyconfr__2019_dot_grpc__nlp_dot_protos_dot_StorageService__pb2.StoreTweetsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pyconfr_2019.grpc_nlp.StorageService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
