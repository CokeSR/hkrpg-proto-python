# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RogueTalent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import RogueTalentStatus_pb2 as RogueTalentStatus__pb2
import RogueUnlockProgress_pb2 as RogueUnlockProgress__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11RogueTalent.proto\x1a\x17RogueTalentStatus.proto\x1a\x19RogueUnlockProgress.proto\"x\n\x0bRogueTalent\x12\"\n\x06status\x18\x05 \x01(\x0e\x32\x12.RogueTalentStatus\x12\x32\n\x14unlock_progress_list\x18\x03 \x03(\x0b\x32\x14.RogueUnlockProgress\x12\x11\n\ttalent_id\x18\x08 \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RogueTalent_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ROGUETALENT']._serialized_start=73
  _globals['_ROGUETALENT']._serialized_end=193
# @@protoc_insertion_point(module_scope)