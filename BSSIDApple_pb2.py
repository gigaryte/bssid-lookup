# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BSSIDApple.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BSSIDApple.proto',
  package='',
  serialized_pb=_b('\n\x10\x42SSIDApple.proto\"\x9b\x03\n\x0cWifiDetected\x12\r\n\x05\x62ssid\x18\x01 \x02(\t\x12(\n\x08location\x18\x02 \x01(\x0b\x32\x16.WifiDetected.Location\x1a\xd1\x02\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x03\x12\x11\n\tlongitude\x18\x02 \x01(\x03\x12\x18\n\x10valeur_inconnue3\x18\x03 \x01(\x03\x12\x18\n\x10valeur_inconnue4\x18\x04 \x01(\x03\x12\x18\n\x10valeur_inconnue5\x18\x05 \x01(\x03\x12\x18\n\x10valeur_inconnue6\x18\x06 \x01(\x03\x12\x18\n\x10valeur_inconnue7\x18\x07 \x01(\x03\x12\x18\n\x10valeur_inconnue8\x18\x08 \x01(\x03\x12\x18\n\x10valeur_inconnue9\x18\t \x01(\x03\x12\x19\n\x11valeur_inconnue10\x18\n \x01(\x03\x12\x19\n\x11valeur_inconnue11\x18\x0b \x01(\x03\x12\x19\n\x11valeur_inconnue12\x18\x0c \x01(\x03\x12\x19\n\x11valeur_inconnue21\x18\x15 \x01(\x03\"\x8d\x01\n\x0f\x42lockBSSIDApple\x12\x18\n\x10valeur_inconnue0\x18\x01 \x01(\x03\x12\x1b\n\x04wifi\x18\x02 \x03(\x0b\x32\r.WifiDetected\x12\x18\n\x10valeur_inconnue1\x18\x03 \x01(\x05\x12\x18\n\x10valeur_inconnue2\x18\x04 \x01(\x05\x12\x0f\n\x07\x41PIName\x18\x05 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_WIFIDETECTED_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='WifiDetected.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='WifiDetected.Location.latitude', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='WifiDetected.Location.longitude', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue3', full_name='WifiDetected.Location.valeur_inconnue3', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue4', full_name='WifiDetected.Location.valeur_inconnue4', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue5', full_name='WifiDetected.Location.valeur_inconnue5', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue6', full_name='WifiDetected.Location.valeur_inconnue6', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue7', full_name='WifiDetected.Location.valeur_inconnue7', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue8', full_name='WifiDetected.Location.valeur_inconnue8', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue9', full_name='WifiDetected.Location.valeur_inconnue9', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue10', full_name='WifiDetected.Location.valeur_inconnue10', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue11', full_name='WifiDetected.Location.valeur_inconnue11', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue12', full_name='WifiDetected.Location.valeur_inconnue12', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue21', full_name='WifiDetected.Location.valeur_inconnue21', index=12,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=432,
)

_WIFIDETECTED = _descriptor.Descriptor(
  name='WifiDetected',
  full_name='WifiDetected',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bssid', full_name='WifiDetected.bssid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='WifiDetected.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_WIFIDETECTED_LOCATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=432,
)


_BLOCKBSSIDAPPLE = _descriptor.Descriptor(
  name='BlockBSSIDApple',
  full_name='BlockBSSIDApple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valeur_inconnue0', full_name='BlockBSSIDApple.valeur_inconnue0', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wifi', full_name='BlockBSSIDApple.wifi', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue1', full_name='BlockBSSIDApple.valeur_inconnue1', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valeur_inconnue2', full_name='BlockBSSIDApple.valeur_inconnue2', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='APIName', full_name='BlockBSSIDApple.APIName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=576,
)

_WIFIDETECTED_LOCATION.containing_type = _WIFIDETECTED
_WIFIDETECTED.fields_by_name['location'].message_type = _WIFIDETECTED_LOCATION
_BLOCKBSSIDAPPLE.fields_by_name['wifi'].message_type = _WIFIDETECTED
DESCRIPTOR.message_types_by_name['WifiDetected'] = _WIFIDETECTED
DESCRIPTOR.message_types_by_name['BlockBSSIDApple'] = _BLOCKBSSIDAPPLE

WifiDetected = _reflection.GeneratedProtocolMessageType('WifiDetected', (_message.Message,), dict(

  Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
    DESCRIPTOR = _WIFIDETECTED_LOCATION,
    __module__ = 'BSSIDApple_pb2'
    # @@protoc_insertion_point(class_scope:WifiDetected.Location)
    ))
  ,
  DESCRIPTOR = _WIFIDETECTED,
  __module__ = 'BSSIDApple_pb2'
  # @@protoc_insertion_point(class_scope:WifiDetected)
  ))
_sym_db.RegisterMessage(WifiDetected)
_sym_db.RegisterMessage(WifiDetected.Location)

BlockBSSIDApple = _reflection.GeneratedProtocolMessageType('BlockBSSIDApple', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKBSSIDAPPLE,
  __module__ = 'BSSIDApple_pb2'
  # @@protoc_insertion_point(class_scope:BlockBSSIDApple)
  ))
_sym_db.RegisterMessage(BlockBSSIDApple)


# @@protoc_insertion_point(module_scope)
