# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messenger.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fmessenger.proto\"\x1a\n\nClientInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x10\x43onnectionStatus\x12\x11\n\tconnected\x18\x01 \x01(\x08\"<\n\x07Message\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"\x07\n\x05\x45mpty\"\x14\n\x04Menu\x12\x0c\n\x04menu\x18\x01 \x01(\t\".\n\x0e\x43\x61tegoryChoice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x63hoice\x18\x02 \x01(\t\"(\n\nItemChoice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04item\x18\x02 \x01(\t2\xec\x01\n\tMessenger\x12)\n\x07\x43onnect\x12\x0b.ClientInfo\x1a\x11.ConnectionStatus\x12\x1f\n\x0bSendMessage\x12\x08.Message\x1a\x06.Empty\x12*\n\x0fReceiveMessages\x12\x0b.ClientInfo\x1a\x08.Message0\x01\x12\x19\n\x08ShowMenu\x12\x06.Empty\x1a\x05.Menu\x12)\n\x0e\x43hooseCategory\x12\x0f.CategoryChoice\x1a\x06.Empty\x12!\n\nChooseItem\x12\x0b.ItemChoice\x1a\x06.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messenger_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CLIENTINFO']._serialized_start=19
  _globals['_CLIENTINFO']._serialized_end=45
  _globals['_CONNECTIONSTATUS']._serialized_start=47
  _globals['_CONNECTIONSTATUS']._serialized_end=84
  _globals['_MESSAGE']._serialized_start=86
  _globals['_MESSAGE']._serialized_end=146
  _globals['_EMPTY']._serialized_start=148
  _globals['_EMPTY']._serialized_end=155
  _globals['_MENU']._serialized_start=157
  _globals['_MENU']._serialized_end=177
  _globals['_CATEGORYCHOICE']._serialized_start=179
  _globals['_CATEGORYCHOICE']._serialized_end=225
  _globals['_ITEMCHOICE']._serialized_start=227
  _globals['_ITEMCHOICE']._serialized_end=267
  _globals['_MESSENGER']._serialized_start=270
  _globals['_MESSENGER']._serialized_end=506
# @@protoc_insertion_point(module_scope)
