# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RotateMapCsReq.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MotionInfo_pb2 as MotionInfo__pb2
import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14RotateMapCsReq.proto\x1a\x10MotionInfo.proto\x1a\x0cVector.proto\"\x86\x02\n\x0eRotateMapCsReq\x12\x0f\n\x07unk_int\x18\x05 \x01(\r\x12\x10\n\x08group_id\x18\x04 \x01(\r\x12\x1b\n\x06motion\x18\x0f \x01(\x0b\x32\x0b.MotionInfo\x12,\n\trogue_map\x18\x0c \x01(\x0b\x32\x19.RotateMapCsReq.NewMapRot\x1a\x35\n\x07Vector4\x12\t\n\x01z\x18\r \x01(\x02\x12\t\n\x01y\x18\t \x01(\x02\x12\t\n\x01x\x18\x07 \x01(\x02\x12\t\n\x01w\x18\x0f \x01(\x02\x1aO\n\tNewMapRot\x12\x18\n\x07vector3\x18\x0f \x01(\x0b\x32\x07.Vector\x12(\n\x07vector4\x18\n \x01(\x0b\x32\x17.RotateMapCsReq.Vector4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RotateMapCsReq_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ROTATEMAPCSREQ']._serialized_start=57
  _globals['_ROTATEMAPCSREQ']._serialized_end=319
  _globals['_ROTATEMAPCSREQ_VECTOR4']._serialized_start=185
  _globals['_ROTATEMAPCSREQ_VECTOR4']._serialized_end=238
  _globals['_ROTATEMAPCSREQ_NEWMAPROT']._serialized_start=240
  _globals['_ROTATEMAPCSREQ_NEWMAPROT']._serialized_end=319
# @@protoc_insertion_point(module_scope)