# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetHeroBasicTypeInfoScRsp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HeroBasicType_pb2 as HeroBasicType__pb2
import Gender_pb2 as Gender__pb2
import HeroBasicTypeInfo_pb2 as HeroBasicTypeInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fGetHeroBasicTypeInfoScRsp.proto\x1a\x13HeroBasicType.proto\x1a\x0cGender.proto\x1a\x17HeroBasicTypeInfo.proto\"\xbd\x01\n\x19GetHeroBasicTypeInfoScRsp\x12&\n\x0e\x63ur_basic_type\x18\x03 \x01(\x0e\x32\x0e.HeroBasicType\x12\x1c\n\x14unlocked_basic_types\x18\x08 \x03(\r\x12\x30\n\x14\x62\x61sic_type_info_list\x18\x0f \x03(\x0b\x32\x12.HeroBasicTypeInfo\x12\x17\n\x06gender\x18\x0b \x01(\x0e\x32\x07.Gender\x12\x0f\n\x07retcode\x18\x02 \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetHeroBasicTypeInfoScRsp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETHEROBASICTYPEINFOSCRSP']._serialized_start=96
  _globals['_GETHEROBASICTYPEINFOSCRSP']._serialized_end=285
# @@protoc_insertion_point(module_scope)
