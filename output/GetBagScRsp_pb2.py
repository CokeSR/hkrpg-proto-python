# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetBagScRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Relic_pb2 as Relic__pb2
import Equipment_pb2 as Equipment__pb2
import Material_pb2 as Material__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11GetBagScRsp.proto\x1a\x0bRelic.proto\x1a\x0f\x45quipment.proto\x1a\x0eMaterial.proto\"\x80\x01\n\x0bGetBagScRsp\x12\x0f\n\x07retcode\x18\n \x01(\r\x12\"\n\x0e\x65quipment_list\x18\x01 \x03(\x0b\x32\n.Equipment\x12\x1a\n\nrelic_list\x18\x0f \x03(\x0b\x32\x06.Relic\x12 \n\rmaterial_list\x18\x02 \x03(\x0b\x32\t.Materialb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetBagScRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETBAGSCRSP']._serialized_start=68
  _globals['_GETBAGSCRSP']._serialized_end=196
# @@protoc_insertion_point(module_scope)