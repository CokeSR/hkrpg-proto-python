# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetMissionStatusScRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Mission_pb2 as Mission__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bGetMissionStatusScRsp.proto\x1a\rMission.proto\"\xf7\x01\n\x15GetMissionStatusScRsp\x12\x0f\n\x07retcode\x18\t \x01(\r\x12%\n\x1d\x66inished_main_mission_id_list\x18\x07 \x03(\r\x12\'\n\x1funfinished_main_mission_id_list\x18\n \x03(\r\x12%\n\x1d\x64isabled_main_mission_id_list\x18\x0f \x03(\r\x12)\n\x17sub_mission_status_list\x18\x04 \x03(\x0b\x32\x08.Mission\x12+\n\x19mission_event_status_list\x18\x0c \x03(\x0b\x32\x08.Missionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetMissionStatusScRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETMISSIONSTATUSSCRSP']._serialized_start=47
  _globals['_GETMISSIONSTATUSSCRSP']._serialized_end=294
# @@protoc_insertion_point(module_scope)
