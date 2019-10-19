# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyconfr_2019.grpc_nlp.protos.Tweet_pb2 import (
    Tweet as pyconfr_2019___grpc_nlp___protos___Tweet_pb2___Tweet,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class StoreTweetsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def tweet(self) -> pyconfr_2019___grpc_nlp___protos___Tweet_pb2___Tweet: ...

    def __init__(self,
        *,
        tweet : typing___Optional[pyconfr_2019___grpc_nlp___protos___Tweet_pb2___Tweet] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> StoreTweetsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"tweet"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"tweet"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"tweet",b"tweet"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"tweet",b"tweet"]) -> None: ...

class StoreTweetsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    nb_tweets_received = ... # type: builtin___int
    nb_tweets_stored = ... # type: builtin___int

    def __init__(self,
        *,
        nb_tweets_received : typing___Optional[builtin___int] = None,
        nb_tweets_stored : typing___Optional[builtin___int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> StoreTweetsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"nb_tweets_received",u"nb_tweets_stored"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"nb_tweets_received",b"nb_tweets_received",u"nb_tweets_stored",b"nb_tweets_stored"]) -> None: ...