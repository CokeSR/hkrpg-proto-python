# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Shop.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Goods_pb2 as Goods__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nShop.proto\x1a\x0bGoods.proto\"\xa0\x01\n\x04Shop\x12\x12\n\ncity_level\x18\x08 \x01(\r\x12\x12\n\nbegin_time\x18\n \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x0f \x01(\x03\x12\x1a\n\ngoods_list\x18\t \x03(\x0b\x32\x06.Goods\x12\x10\n\x08\x63ity_exp\x18\x02 \x01(\r\x12\x1f\n\x17\x63ity_taken_level_reward\x18\x04 \x01(\x04\x12\x0f\n\x07shop_id\x18\x0e \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Shop_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SHOP']._serialized_start=28
  _globals['_SHOP']._serialized_end=188
# @@protoc_insertion_point(module_scope)
