# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GachaItem.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Item_pb2 as Item__pb2
import ItemList_pb2 as ItemList__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fGachaItem.proto\x1a\nItem.proto\x1a\x0eItemList.proto\"|\n\tGachaItem\x12\x1d\n\ntoken_item\x18\x08 \x01(\x0b\x32\t.ItemList\x12\x0e\n\x06is_new\x18\n \x01(\x08\x12\x19\n\ngacha_item\x18\r \x01(\x0b\x32\x05.Item\x12%\n\x12transfer_item_list\x18\x0f \x01(\x0b\x32\t.ItemListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GachaItem_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GACHAITEM']._serialized_start=47
  _globals['_GACHAITEM']._serialized_end=171
# @@protoc_insertion_point(module_scope)
