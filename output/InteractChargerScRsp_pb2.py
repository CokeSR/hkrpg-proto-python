# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: InteractChargerScRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ChargerInfo_pb2 as ChargerInfo__pb2
import RotatorEnergyInfo_pb2 as RotatorEnergyInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aInteractChargerScRsp.proto\x1a\x11\x43hargerInfo.proto\x1a\x17RotatorEnergyInfo.proto\"t\n\x14InteractChargerScRsp\x12\x0f\n\x07retcode\x18\x0e \x01(\r\x12\"\n\x0c\x63harger_info\x18\x06 \x01(\x0b\x32\x0c.ChargerInfo\x12\'\n\x0b\x65nergy_info\x18\x0c \x01(\x0b\x32\x12.RotatorEnergyInfob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'InteractChargerScRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INTERACTCHARGERSCRSP']._serialized_start=74
  _globals['_INTERACTCHARGERSCRSP']._serialized_end=190
# @@protoc_insertion_point(module_scope)
