# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SwapLineupCsReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ExtraLineupType_pb2 as ExtraLineupType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15SwapLineupCsReq.proto\x1a\x15\x45xtraLineupType.proto\"\x97\x01\n\x0fSwapLineupCsReq\x12+\n\x11\x65xtra_lineup_type\x18\x0c \x01(\x0e\x32\x10.ExtraLineupType\x12\x10\n\x08plane_id\x18\x08 \x01(\r\x12\r\n\x05index\x18\x04 \x01(\r\x12\x10\n\x08src_slot\x18\x03 \x01(\r\x12\x12\n\nis_virtual\x18\n \x01(\x08\x12\x10\n\x08\x64st_slot\x18\t \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SwapLineupCsReq_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SWAPLINEUPCSREQ']._serialized_start=49
  _globals['_SWAPLINEUPCSREQ']._serialized_end=200
# @@protoc_insertion_point(module_scope)
