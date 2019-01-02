# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dag.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dag.proto',
  package='dag',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tdag.proto\x12\x03\x64\x61g\"k\n\x07\x44\x41GNode\x12\x1d\n\x06\x63ommit\x18\x01 \x01(\x0b\x32\x0b.dag.CommitH\x00\x12\x19\n\x04tree\x18\x02 \x01(\x0b\x32\t.dag.TreeH\x00\x12\x19\n\x04\x62lob\x18\x03 \x01(\x0b\x32\t.dag.BlobH\x00\x42\x0b\n\tnode_type\"\x08\n\x06\x43ommit\"=\n\x10TreeLinkMetadata\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.dag.NodeType\x12\x0c\n\x04name\x18\x02 \x01(\t\"I\n\x04Tree\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.dag.NodeType\x12$\n\x05mdata\x18\x02 \x03(\x0b\x32\x15.dag.TreeLinkMetadata\"\x14\n\x04\x42lob\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c*#\n\x08NodeType\x12\r\n\tNAMESPACE\x10\x00\x12\x08\n\x04\x44\x41TA\x10\x01\x62\x06proto3')
)

_NODETYPE = _descriptor.EnumDescriptor(
  name='NodeType',
  full_name='dag.NodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NAMESPACE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=297,
  serialized_end=332,
)
_sym_db.RegisterEnumDescriptor(_NODETYPE)

NodeType = enum_type_wrapper.EnumTypeWrapper(_NODETYPE)
NAMESPACE = 0
DATA = 1



_DAGNODE = _descriptor.Descriptor(
  name='DAGNode',
  full_name='dag.DAGNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='commit', full_name='dag.DAGNode.commit', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tree', full_name='dag.DAGNode.tree', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blob', full_name='dag.DAGNode.blob', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='node_type', full_name='dag.DAGNode.node_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=18,
  serialized_end=125,
)


_COMMIT = _descriptor.Descriptor(
  name='Commit',
  full_name='dag.Commit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=127,
  serialized_end=135,
)


_TREELINKMETADATA = _descriptor.Descriptor(
  name='TreeLinkMetadata',
  full_name='dag.TreeLinkMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dag.TreeLinkMetadata.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dag.TreeLinkMetadata.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=137,
  serialized_end=198,
)


_TREE = _descriptor.Descriptor(
  name='Tree',
  full_name='dag.Tree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dag.Tree.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mdata', full_name='dag.Tree.mdata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=200,
  serialized_end=273,
)


_BLOB = _descriptor.Descriptor(
  name='Blob',
  full_name='dag.Blob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='dag.Blob.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=275,
  serialized_end=295,
)

_DAGNODE.fields_by_name['commit'].message_type = _COMMIT
_DAGNODE.fields_by_name['tree'].message_type = _TREE
_DAGNODE.fields_by_name['blob'].message_type = _BLOB
_DAGNODE.oneofs_by_name['node_type'].fields.append(
  _DAGNODE.fields_by_name['commit'])
_DAGNODE.fields_by_name['commit'].containing_oneof = _DAGNODE.oneofs_by_name['node_type']
_DAGNODE.oneofs_by_name['node_type'].fields.append(
  _DAGNODE.fields_by_name['tree'])
_DAGNODE.fields_by_name['tree'].containing_oneof = _DAGNODE.oneofs_by_name['node_type']
_DAGNODE.oneofs_by_name['node_type'].fields.append(
  _DAGNODE.fields_by_name['blob'])
_DAGNODE.fields_by_name['blob'].containing_oneof = _DAGNODE.oneofs_by_name['node_type']
_TREELINKMETADATA.fields_by_name['type'].enum_type = _NODETYPE
_TREE.fields_by_name['type'].enum_type = _NODETYPE
_TREE.fields_by_name['mdata'].message_type = _TREELINKMETADATA
DESCRIPTOR.message_types_by_name['DAGNode'] = _DAGNODE
DESCRIPTOR.message_types_by_name['Commit'] = _COMMIT
DESCRIPTOR.message_types_by_name['TreeLinkMetadata'] = _TREELINKMETADATA
DESCRIPTOR.message_types_by_name['Tree'] = _TREE
DESCRIPTOR.message_types_by_name['Blob'] = _BLOB
DESCRIPTOR.enum_types_by_name['NodeType'] = _NODETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DAGNode = _reflection.GeneratedProtocolMessageType('DAGNode', (_message.Message,), dict(
  DESCRIPTOR = _DAGNODE,
  __module__ = 'dag_pb2'
  # @@protoc_insertion_point(class_scope:dag.DAGNode)
  ))
_sym_db.RegisterMessage(DAGNode)

Commit = _reflection.GeneratedProtocolMessageType('Commit', (_message.Message,), dict(
  DESCRIPTOR = _COMMIT,
  __module__ = 'dag_pb2'
  # @@protoc_insertion_point(class_scope:dag.Commit)
  ))
_sym_db.RegisterMessage(Commit)

TreeLinkMetadata = _reflection.GeneratedProtocolMessageType('TreeLinkMetadata', (_message.Message,), dict(
  DESCRIPTOR = _TREELINKMETADATA,
  __module__ = 'dag_pb2'
  # @@protoc_insertion_point(class_scope:dag.TreeLinkMetadata)
  ))
_sym_db.RegisterMessage(TreeLinkMetadata)

Tree = _reflection.GeneratedProtocolMessageType('Tree', (_message.Message,), dict(
  DESCRIPTOR = _TREE,
  __module__ = 'dag_pb2'
  # @@protoc_insertion_point(class_scope:dag.Tree)
  ))
_sym_db.RegisterMessage(Tree)

Blob = _reflection.GeneratedProtocolMessageType('Blob', (_message.Message,), dict(
  DESCRIPTOR = _BLOB,
  __module__ = 'dag_pb2'
  # @@protoc_insertion_point(class_scope:dag.Blob)
  ))
_sym_db.RegisterMessage(Blob)


# @@protoc_insertion_point(module_scope)