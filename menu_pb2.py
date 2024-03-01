# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: menu.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='menu.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmenu.proto\"%\n\x08MenuItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"0\n\x04Menu\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x18\n\x05items\x18\x02 \x03(\x0b\x32\t.MenuItemb\x06proto3'
)




_MENUITEM = _descriptor.Descriptor(
  name='MenuItem',
  full_name='MenuItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MenuItem.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='MenuItem.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=51,
)


_MENU = _descriptor.Descriptor(
  name='Menu',
  full_name='Menu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='Menu.header', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='Menu.items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=101,
)

_MENU.fields_by_name['items'].message_type = _MENUITEM
DESCRIPTOR.message_types_by_name['MenuItem'] = _MENUITEM
DESCRIPTOR.message_types_by_name['Menu'] = _MENU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MenuItem = _reflection.GeneratedProtocolMessageType('MenuItem', (_message.Message,), {
  'DESCRIPTOR' : _MENUITEM,
  '__module__' : 'menu_pb2'
  # @@protoc_insertion_point(class_scope:MenuItem)
  })
_sym_db.RegisterMessage(MenuItem)

Menu = _reflection.GeneratedProtocolMessageType('Menu', (_message.Message,), {
  'DESCRIPTOR' : _MENU,
  '__module__' : 'menu_pb2'
  # @@protoc_insertion_point(class_scope:Menu)
  })
_sym_db.RegisterMessage(Menu)


# @@protoc_insertion_point(module_scope)
