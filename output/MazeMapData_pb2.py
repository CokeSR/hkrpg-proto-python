# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MazeMapData.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MazeGroup_pb2 as MazeGroup__pb2
import MazeChest_pb2 as MazeChest__pb2
import MazeProp_pb2 as MazeProp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11MazeMapData.proto\x1a\x0fMazeGroup.proto\x1a\x0fMazeChest.proto\x1a\x0eMazeProp.proto\"\xf9\x01\n\x0bMazeMapData\x12\'\n\x13unlocked_chest_list\x18\t \x03(\x0b\x32\n.MazeChest\x12#\n\x0fmaze_group_list\x18\x0e \x03(\x0b\x32\n.MazeGroup\x12\x0f\n\x07retcode\x18\x01 \x01(\r\x12!\n\x0emaze_prop_list\x18\x03 \x03(\x0b\x32\t.MazeProp\x12\x1c\n\x14lighten_section_list\x18\x0c \x03(\r\x12\x1e\n\x16unlocked_teleport_list\x18\n \x03(\r\x12\x18\n\x10\x63ur_map_entry_id\x18\x02 \x01(\r\x12\x10\n\x08\x65ntry_id\x18\x05 \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MazeMapData_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MAZEMAPDATA']._serialized_start=72
  _globals['_MAZEMAPDATA']._serialized_end=321
# @@protoc_insertion_point(module_scope)
