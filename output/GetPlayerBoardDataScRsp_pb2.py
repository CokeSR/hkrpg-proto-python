# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetPlayerBoardDataScRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HeadIcon_pb2 as HeadIcon__pb2
import DisplayAvatarVec_pb2 as DisplayAvatarVec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dGetPlayerBoardDataScRsp.proto\x1a\x0eHeadIcon.proto\x1a\x16\x44isplayAvatarVec.proto\"\xda\x01\n\x17GetPlayerBoardDataScRsp\x12\x11\n\tsignature\x18\x01 \x01(\t\x12*\n\x17unlocked_head_icon_list\x18\x0b \x03(\x0b\x32\t.HeadIcon\x12\"\n\x1a\x64isplay_support_avatar_vec\x18\r \x03(\r\x12\x1c\n\x14\x63urrent_head_icon_id\x18\x05 \x01(\r\x12-\n\x12\x64isplay_avatar_vec\x18\x0f \x01(\x0b\x32\x11.DisplayAvatarVec\x12\x0f\n\x07retcode\x18\x0c \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetPlayerBoardDataScRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETPLAYERBOARDDATASCRSP']._serialized_start=74
  _globals['_GETPLAYERBOARDDATASCRSP']._serialized_end=292
# @@protoc_insertion_point(module_scope)