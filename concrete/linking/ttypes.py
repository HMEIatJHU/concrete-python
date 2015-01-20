#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import concrete.uuid.ttypes
import concrete.metadata.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class LinkTarget(object):
  """
  A structure that represents the target of an entity linking annotation.

  Attributes:
   - confidence: Confidence of this LinkTarget object.
   - targetId: A UUID that represents the target of this LinkTarget. This
  UUID should exist in the Entity/Situation(Mention)Set that the
  Linking object is contained in.
   - dbId: A database ID that represents the target of this linking.

  This should be used if the target of the linking is not associated
  with an Entity|Situation(Mention)Set in Concrete, and therefore cannot be linked by
  a UUID internal to concrete.

  If present, other optional field 'dbName' should also be populated.
   - dbName: The name of the database that represents the target of this linking.

  Together with the 'dbId', this can form a pointer to a target
  that is not represented inside concrete.

  Should be populated alongside 'dbId'.
  """

  thrift_spec = (
    None, # 0
    (1, TType.DOUBLE, 'confidence', None, None, ), # 1
    (2, TType.STRUCT, 'targetId', (concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec), None, ), # 2
    (3, TType.STRING, 'dbId', None, None, ), # 3
    (4, TType.STRING, 'dbName', None, None, ), # 4
  )

  def __init__(self, confidence=None, targetId=None, dbId=None, dbName=None,):
    self.confidence = confidence
    self.targetId = targetId
    self.dbId = dbId
    self.dbName = dbName

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.DOUBLE:
          self.confidence = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.targetId = concrete.uuid.ttypes.UUID()
          self.targetId.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.dbId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.dbName = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LinkTarget')
    if self.confidence is not None:
      oprot.writeFieldBegin('confidence', TType.DOUBLE, 1)
      oprot.writeDouble(self.confidence)
      oprot.writeFieldEnd()
    if self.targetId is not None:
      oprot.writeFieldBegin('targetId', TType.STRUCT, 2)
      self.targetId.write(oprot)
      oprot.writeFieldEnd()
    if self.dbId is not None:
      oprot.writeFieldBegin('dbId', TType.STRING, 3)
      oprot.writeString(self.dbId.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.dbName is not None:
      oprot.writeFieldBegin('dbName', TType.STRING, 4)
      oprot.writeString(self.dbName.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.confidence)
    value = (value * 31) ^ hash(self.targetId)
    value = (value * 31) ^ hash(self.dbId)
    value = (value * 31) ^ hash(self.dbName)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Link(object):
  """
  A structure that represents the origin of an entity linking annotation.

  Attributes:
   - sourceId: The "root" of this Link; points to a EntityMention UUID, Entity UUID, etc.
   - linkTargetList: A list of LinkTarget objects that this Link contains.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'sourceId', (concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec), None, ), # 1
    (2, TType.LIST, 'linkTargetList', (TType.STRUCT,(LinkTarget, LinkTarget.thrift_spec)), None, ), # 2
  )

  def __init__(self, sourceId=None, linkTargetList=None,):
    self.sourceId = sourceId
    self.linkTargetList = linkTargetList

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.sourceId = concrete.uuid.ttypes.UUID()
          self.sourceId.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.linkTargetList = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = LinkTarget()
            _elem5.read(iprot)
            self.linkTargetList.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Link')
    if self.sourceId is not None:
      oprot.writeFieldBegin('sourceId', TType.STRUCT, 1)
      self.sourceId.write(oprot)
      oprot.writeFieldEnd()
    if self.linkTargetList is not None:
      oprot.writeFieldBegin('linkTargetList', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.linkTargetList))
      for iter6 in self.linkTargetList:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.sourceId is None:
      raise TProtocol.TProtocolException(message='Required field sourceId is unset!')
    if self.linkTargetList is None:
      raise TProtocol.TProtocolException(message='Required field linkTargetList is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.sourceId)
    value = (value * 31) ^ hash(self.linkTargetList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Linking(object):
  """
  A structure that represents entity linking annotations.

  Attributes:
   - metadata: Metadata related to this Linking object.
   - linkList: A list of Link objects that this Linking object contains.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'metadata', (concrete.metadata.ttypes.AnnotationMetadata, concrete.metadata.ttypes.AnnotationMetadata.thrift_spec), None, ), # 1
    (2, TType.LIST, 'linkList', (TType.STRUCT,(Link, Link.thrift_spec)), None, ), # 2
  )

  def __init__(self, metadata=None, linkList=None,):
    self.metadata = metadata
    self.linkList = linkList

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.metadata = concrete.metadata.ttypes.AnnotationMetadata()
          self.metadata.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.linkList = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = Link()
            _elem12.read(iprot)
            self.linkList.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Linking')
    if self.metadata is not None:
      oprot.writeFieldBegin('metadata', TType.STRUCT, 1)
      self.metadata.write(oprot)
      oprot.writeFieldEnd()
    if self.linkList is not None:
      oprot.writeFieldBegin('linkList', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.linkList))
      for iter13 in self.linkList:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.metadata is None:
      raise TProtocol.TProtocolException(message='Required field metadata is unset!')
    if self.linkList is None:
      raise TProtocol.TProtocolException(message='Required field linkList is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.metadata)
    value = (value * 31) ^ hash(self.linkList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)