# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LineupInfo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ExtraLineupType_pb2 as ExtraLineupType__pb2
import LineupAvatar_pb2 as LineupAvatar__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10LineupInfo.proto\x1a\x15\x45xtraLineupType.proto\x1a\x12LineupAvatar.proto\"\xd1\x01\n\nLineupInfo\x12\x10\n\x08plane_id\x18\x03 \x01(\r\x12\"\n\x0b\x61vatar_list\x18\x07 \x03(\x0b\x32\r.LineupAvatar\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\r\n\x05index\x18\r \x01(\r\x12\x13\n\x0bleader_slot\x18\x0c \x01(\r\x12+\n\x11\x65xtra_lineup_type\x18\n \x01(\x0e\x32\x10.ExtraLineupType\x12\x12\n\nis_virtual\x18\x02 \x01(\x08\x12\x0e\n\x06max_mp\x18\t \x01(\r\x12\n\n\x02mp\x18\x0b \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'LineupInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LINEUPINFO']._serialized_start=64
  _globals['_LINEUPINFO']._serialized_end=273
# @@protoc_insertion_point(module_scope)
