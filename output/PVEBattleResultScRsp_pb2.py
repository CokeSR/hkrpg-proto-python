# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PVEBattleResultScRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import BattleEndStatus_pb2 as BattleEndStatus__pb2
import BattleAvatar_pb2 as BattleAvatar__pb2
import ItemList_pb2 as ItemList__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aPVEBattleResultScRsp.proto\x1a\x15\x42\x61ttleEndStatus.proto\x1a\x12\x42\x61ttleAvatar.proto\x1a\x0eItemList.proto\"\xf9\x02\n\x14PVEBattleResultScRsp\x12\x17\n\x0f\x63heck_identical\x18\x08 \x01(\x08\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\r\x12)\n\x12\x62\x61ttle_avatar_list\x18\x0f \x03(\x0b\x32\r.BattleAvatar\x12\x11\n\tbattle_id\x18\x04 \x01(\r\x12\x0f\n\x07retcode\x18\x0c \x01(\r\x12\x13\n\x0b\x62in_version\x18\r \x01(\t\x12$\n\nend_status\x18\x0b \x01(\x0e\x32\x10.BattleEndStatus\x12\x13\n\x0bres_version\x18\x05 \x01(\t\x12\x10\n\x08stage_id\x18\x07 \x01(\r\x12\x1b\n\x13mismatch_turn_count\x18\x06 \x01(\r\x12\x1c\n\tdrop_data\x18\x01 \x01(\x0b\x32\t.ItemList\x12\x17\n\x04unk1\x18\x03 \x01(\x0b\x32\t.ItemList\x12\x17\n\x04unk2\x18\n \x01(\x0b\x32\t.ItemList\x12\x18\n\x04unk3\x18\xfd\x01 \x01(\x0b\x32\t.ItemListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PVEBattleResultScRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PVEBATTLERESULTSCRSP']._serialized_start=90
  _globals['_PVEBATTLERESULTSCRSP']._serialized_end=467
# @@protoc_insertion_point(module_scope)
