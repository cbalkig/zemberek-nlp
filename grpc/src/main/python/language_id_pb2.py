# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language_id.proto

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
  name='language_id.proto',
  package='zemberek.langid',
  syntax='proto3',
  serialized_pb=_b('\n\x11language_id.proto\x12\x0fzemberek.langid\"6\n\rDetectRequest\x12\r\n\x05input\x18\x01 \x01(\t\x12\x16\n\x0emaxSampleCount\x18\x02 \x01(\x05\" \n\x0e\x44\x65tectResponse\x12\x0e\n\x06langId\x18\x01 \x01(\t2\xad\x01\n\x11LanguageIdService\x12I\n\x06\x44\x65tect\x12\x1e.zemberek.langid.DetectRequest\x1a\x1f.zemberek.langid.DetectResponse\x12M\n\nDetectFast\x12\x1e.zemberek.langid.DetectRequest\x1a\x1f.zemberek.langid.DetectResponseB\x12\n\x0ezemberek.protoP\x01\x62\x06proto3')
)




_DETECTREQUEST = _descriptor.Descriptor(
  name='DetectRequest',
  full_name='zemberek.langid.DetectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='zemberek.langid.DetectRequest.input', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxSampleCount', full_name='zemberek.langid.DetectRequest.maxSampleCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=92,
)


_DETECTRESPONSE = _descriptor.Descriptor(
  name='DetectResponse',
  full_name='zemberek.langid.DetectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='langId', full_name='zemberek.langid.DetectResponse.langId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=126,
)

DESCRIPTOR.message_types_by_name['DetectRequest'] = _DETECTREQUEST
DESCRIPTOR.message_types_by_name['DetectResponse'] = _DETECTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DetectRequest = _reflection.GeneratedProtocolMessageType('DetectRequest', (_message.Message,), dict(
  DESCRIPTOR = _DETECTREQUEST,
  __module__ = 'language_id_pb2'
  # @@protoc_insertion_point(class_scope:zemberek.langid.DetectRequest)
  ))
_sym_db.RegisterMessage(DetectRequest)

DetectResponse = _reflection.GeneratedProtocolMessageType('DetectResponse', (_message.Message,), dict(
  DESCRIPTOR = _DETECTRESPONSE,
  __module__ = 'language_id_pb2'
  # @@protoc_insertion_point(class_scope:zemberek.langid.DetectResponse)
  ))
_sym_db.RegisterMessage(DetectResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\016zemberek.protoP\001'))

_LANGUAGEIDSERVICE = _descriptor.ServiceDescriptor(
  name='LanguageIdService',
  full_name='zemberek.langid.LanguageIdService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=129,
  serialized_end=302,
  methods=[
  _descriptor.MethodDescriptor(
    name='Detect',
    full_name='zemberek.langid.LanguageIdService.Detect',
    index=0,
    containing_service=None,
    input_type=_DETECTREQUEST,
    output_type=_DETECTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DetectFast',
    full_name='zemberek.langid.LanguageIdService.DetectFast',
    index=1,
    containing_service=None,
    input_type=_DETECTREQUEST,
    output_type=_DETECTRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LANGUAGEIDSERVICE)

DESCRIPTOR.services_by_name['LanguageIdService'] = _LANGUAGEIDSERVICE

# @@protoc_insertion_point(module_scope)