# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Chat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MsgType_pb2 as MsgType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nChat.proto\x1a\rMsgType.proto\"f\n\x04\x43hat\x12\r\n\x05\x65mote\x18\x01 \x01(\r\x12\x1a\n\x08msg_type\x18\n \x01(\x0e\x32\x08.MsgType\x12\x12\n\nsender_uid\x18\x07 \x01(\r\x12\x11\n\tsent_time\x18\x02 \x01(\x04\x12\x0c\n\x04text\x18\x05 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Chat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CHAT']._serialized_start=29
  _globals['_CHAT']._serialized_end=131
# @@protoc_insertion_point(module_scope)
