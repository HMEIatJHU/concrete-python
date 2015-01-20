#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import concrete.uuid.ttypes
import concrete.twitter.ttypes
import concrete.email.ttypes
import concrete.nitf.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class TheoryDependencies(object):
  """
  A struct that holds UUIDs for all theories that a particular
  annotation was based upon (and presumably requires).

  Producers of TheoryDependencies should list all stages that they
  used in constructing their particular annotation. They do not,
  however, need to explicitly label *each* stage; they can label
  only the immediate stage before them.

  Examples:

  If you are producing a Tokenization, and only used the
  SentenceSegmentation in order to produce that Tokenization, list
  only the single SentenceSegmentation UUID in sentenceTheoryList.

  In this example, even though the SentenceSegmentation will have
  a dependency on some SectionSegmentation, it is not necessary
  for the Tokenization to list the SectionSegmentation UUID as a
  dependency.

  If you are a producer of EntityMentions, and you use two
  POSTokenTagging and one NERTokenTagging objects, add the UUIDs for
  the POSTokenTagging objects to posTagTheoryList, and the UUID of
  the NER TokenTagging to the nerTagTheoryList.

  In this example, because multiple annotations influenced the
  new annotation, they should all be listed as dependencies.

  Attributes:
   - sectionTheoryList
   - sentenceTheoryList
   - tokenizationTheoryList
   - posTagTheoryList
   - nerTagTheoryList
   - lemmaTheoryList
   - langIdTheoryList
   - parseTheoryList
   - dependencyParseTheoryList
   - tokenAnnotationTheoryList
   - entityMentionSetTheoryList
   - entitySetTheoryList
   - situationMentionSetTheoryList
   - situationSetTheoryList
   - communicationsList
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'sectionTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 1
    (2, TType.LIST, 'sentenceTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'tokenizationTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 3
    (4, TType.LIST, 'posTagTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 4
    (5, TType.LIST, 'nerTagTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 5
    (6, TType.LIST, 'lemmaTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 6
    (7, TType.LIST, 'langIdTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 7
    (8, TType.LIST, 'parseTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 8
    (9, TType.LIST, 'dependencyParseTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 9
    (10, TType.LIST, 'tokenAnnotationTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 10
    (11, TType.LIST, 'entityMentionSetTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 11
    (12, TType.LIST, 'entitySetTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 12
    (13, TType.LIST, 'situationMentionSetTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 13
    (14, TType.LIST, 'situationSetTheoryList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 14
    (15, TType.LIST, 'communicationsList', (TType.STRUCT,(concrete.uuid.ttypes.UUID, concrete.uuid.ttypes.UUID.thrift_spec)), None, ), # 15
  )

  def __init__(self, sectionTheoryList=None, sentenceTheoryList=None, tokenizationTheoryList=None, posTagTheoryList=None, nerTagTheoryList=None, lemmaTheoryList=None, langIdTheoryList=None, parseTheoryList=None, dependencyParseTheoryList=None, tokenAnnotationTheoryList=None, entityMentionSetTheoryList=None, entitySetTheoryList=None, situationMentionSetTheoryList=None, situationSetTheoryList=None, communicationsList=None,):
    self.sectionTheoryList = sectionTheoryList
    self.sentenceTheoryList = sentenceTheoryList
    self.tokenizationTheoryList = tokenizationTheoryList
    self.posTagTheoryList = posTagTheoryList
    self.nerTagTheoryList = nerTagTheoryList
    self.lemmaTheoryList = lemmaTheoryList
    self.langIdTheoryList = langIdTheoryList
    self.parseTheoryList = parseTheoryList
    self.dependencyParseTheoryList = dependencyParseTheoryList
    self.tokenAnnotationTheoryList = tokenAnnotationTheoryList
    self.entityMentionSetTheoryList = entityMentionSetTheoryList
    self.entitySetTheoryList = entitySetTheoryList
    self.situationMentionSetTheoryList = situationMentionSetTheoryList
    self.situationSetTheoryList = situationSetTheoryList
    self.communicationsList = communicationsList

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
        if ftype == TType.LIST:
          self.sectionTheoryList = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = concrete.uuid.ttypes.UUID()
            _elem5.read(iprot)
            self.sectionTheoryList.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.sentenceTheoryList = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = concrete.uuid.ttypes.UUID()
            _elem11.read(iprot)
            self.sentenceTheoryList.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.tokenizationTheoryList = []
          (_etype15, _size12) = iprot.readListBegin()
          for _i16 in xrange(_size12):
            _elem17 = concrete.uuid.ttypes.UUID()
            _elem17.read(iprot)
            self.tokenizationTheoryList.append(_elem17)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.posTagTheoryList = []
          (_etype21, _size18) = iprot.readListBegin()
          for _i22 in xrange(_size18):
            _elem23 = concrete.uuid.ttypes.UUID()
            _elem23.read(iprot)
            self.posTagTheoryList.append(_elem23)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.nerTagTheoryList = []
          (_etype27, _size24) = iprot.readListBegin()
          for _i28 in xrange(_size24):
            _elem29 = concrete.uuid.ttypes.UUID()
            _elem29.read(iprot)
            self.nerTagTheoryList.append(_elem29)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.lemmaTheoryList = []
          (_etype33, _size30) = iprot.readListBegin()
          for _i34 in xrange(_size30):
            _elem35 = concrete.uuid.ttypes.UUID()
            _elem35.read(iprot)
            self.lemmaTheoryList.append(_elem35)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.langIdTheoryList = []
          (_etype39, _size36) = iprot.readListBegin()
          for _i40 in xrange(_size36):
            _elem41 = concrete.uuid.ttypes.UUID()
            _elem41.read(iprot)
            self.langIdTheoryList.append(_elem41)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.LIST:
          self.parseTheoryList = []
          (_etype45, _size42) = iprot.readListBegin()
          for _i46 in xrange(_size42):
            _elem47 = concrete.uuid.ttypes.UUID()
            _elem47.read(iprot)
            self.parseTheoryList.append(_elem47)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.LIST:
          self.dependencyParseTheoryList = []
          (_etype51, _size48) = iprot.readListBegin()
          for _i52 in xrange(_size48):
            _elem53 = concrete.uuid.ttypes.UUID()
            _elem53.read(iprot)
            self.dependencyParseTheoryList.append(_elem53)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.LIST:
          self.tokenAnnotationTheoryList = []
          (_etype57, _size54) = iprot.readListBegin()
          for _i58 in xrange(_size54):
            _elem59 = concrete.uuid.ttypes.UUID()
            _elem59.read(iprot)
            self.tokenAnnotationTheoryList.append(_elem59)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.LIST:
          self.entityMentionSetTheoryList = []
          (_etype63, _size60) = iprot.readListBegin()
          for _i64 in xrange(_size60):
            _elem65 = concrete.uuid.ttypes.UUID()
            _elem65.read(iprot)
            self.entityMentionSetTheoryList.append(_elem65)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.LIST:
          self.entitySetTheoryList = []
          (_etype69, _size66) = iprot.readListBegin()
          for _i70 in xrange(_size66):
            _elem71 = concrete.uuid.ttypes.UUID()
            _elem71.read(iprot)
            self.entitySetTheoryList.append(_elem71)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.LIST:
          self.situationMentionSetTheoryList = []
          (_etype75, _size72) = iprot.readListBegin()
          for _i76 in xrange(_size72):
            _elem77 = concrete.uuid.ttypes.UUID()
            _elem77.read(iprot)
            self.situationMentionSetTheoryList.append(_elem77)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.LIST:
          self.situationSetTheoryList = []
          (_etype81, _size78) = iprot.readListBegin()
          for _i82 in xrange(_size78):
            _elem83 = concrete.uuid.ttypes.UUID()
            _elem83.read(iprot)
            self.situationSetTheoryList.append(_elem83)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.LIST:
          self.communicationsList = []
          (_etype87, _size84) = iprot.readListBegin()
          for _i88 in xrange(_size84):
            _elem89 = concrete.uuid.ttypes.UUID()
            _elem89.read(iprot)
            self.communicationsList.append(_elem89)
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
    oprot.writeStructBegin('TheoryDependencies')
    if self.sectionTheoryList is not None:
      oprot.writeFieldBegin('sectionTheoryList', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.sectionTheoryList))
      for iter90 in self.sectionTheoryList:
        iter90.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.sentenceTheoryList is not None:
      oprot.writeFieldBegin('sentenceTheoryList', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.sentenceTheoryList))
      for iter91 in self.sentenceTheoryList:
        iter91.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.tokenizationTheoryList is not None:
      oprot.writeFieldBegin('tokenizationTheoryList', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.tokenizationTheoryList))
      for iter92 in self.tokenizationTheoryList:
        iter92.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.posTagTheoryList is not None:
      oprot.writeFieldBegin('posTagTheoryList', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.posTagTheoryList))
      for iter93 in self.posTagTheoryList:
        iter93.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.nerTagTheoryList is not None:
      oprot.writeFieldBegin('nerTagTheoryList', TType.LIST, 5)
      oprot.writeListBegin(TType.STRUCT, len(self.nerTagTheoryList))
      for iter94 in self.nerTagTheoryList:
        iter94.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.lemmaTheoryList is not None:
      oprot.writeFieldBegin('lemmaTheoryList', TType.LIST, 6)
      oprot.writeListBegin(TType.STRUCT, len(self.lemmaTheoryList))
      for iter95 in self.lemmaTheoryList:
        iter95.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.langIdTheoryList is not None:
      oprot.writeFieldBegin('langIdTheoryList', TType.LIST, 7)
      oprot.writeListBegin(TType.STRUCT, len(self.langIdTheoryList))
      for iter96 in self.langIdTheoryList:
        iter96.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.parseTheoryList is not None:
      oprot.writeFieldBegin('parseTheoryList', TType.LIST, 8)
      oprot.writeListBegin(TType.STRUCT, len(self.parseTheoryList))
      for iter97 in self.parseTheoryList:
        iter97.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.dependencyParseTheoryList is not None:
      oprot.writeFieldBegin('dependencyParseTheoryList', TType.LIST, 9)
      oprot.writeListBegin(TType.STRUCT, len(self.dependencyParseTheoryList))
      for iter98 in self.dependencyParseTheoryList:
        iter98.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.tokenAnnotationTheoryList is not None:
      oprot.writeFieldBegin('tokenAnnotationTheoryList', TType.LIST, 10)
      oprot.writeListBegin(TType.STRUCT, len(self.tokenAnnotationTheoryList))
      for iter99 in self.tokenAnnotationTheoryList:
        iter99.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.entityMentionSetTheoryList is not None:
      oprot.writeFieldBegin('entityMentionSetTheoryList', TType.LIST, 11)
      oprot.writeListBegin(TType.STRUCT, len(self.entityMentionSetTheoryList))
      for iter100 in self.entityMentionSetTheoryList:
        iter100.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.entitySetTheoryList is not None:
      oprot.writeFieldBegin('entitySetTheoryList', TType.LIST, 12)
      oprot.writeListBegin(TType.STRUCT, len(self.entitySetTheoryList))
      for iter101 in self.entitySetTheoryList:
        iter101.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.situationMentionSetTheoryList is not None:
      oprot.writeFieldBegin('situationMentionSetTheoryList', TType.LIST, 13)
      oprot.writeListBegin(TType.STRUCT, len(self.situationMentionSetTheoryList))
      for iter102 in self.situationMentionSetTheoryList:
        iter102.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.situationSetTheoryList is not None:
      oprot.writeFieldBegin('situationSetTheoryList', TType.LIST, 14)
      oprot.writeListBegin(TType.STRUCT, len(self.situationSetTheoryList))
      for iter103 in self.situationSetTheoryList:
        iter103.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.communicationsList is not None:
      oprot.writeFieldBegin('communicationsList', TType.LIST, 15)
      oprot.writeListBegin(TType.STRUCT, len(self.communicationsList))
      for iter104 in self.communicationsList:
        iter104.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.sectionTheoryList)
    value = (value * 31) ^ hash(self.sentenceTheoryList)
    value = (value * 31) ^ hash(self.tokenizationTheoryList)
    value = (value * 31) ^ hash(self.posTagTheoryList)
    value = (value * 31) ^ hash(self.nerTagTheoryList)
    value = (value * 31) ^ hash(self.lemmaTheoryList)
    value = (value * 31) ^ hash(self.langIdTheoryList)
    value = (value * 31) ^ hash(self.parseTheoryList)
    value = (value * 31) ^ hash(self.dependencyParseTheoryList)
    value = (value * 31) ^ hash(self.tokenAnnotationTheoryList)
    value = (value * 31) ^ hash(self.entityMentionSetTheoryList)
    value = (value * 31) ^ hash(self.entitySetTheoryList)
    value = (value * 31) ^ hash(self.situationMentionSetTheoryList)
    value = (value * 31) ^ hash(self.situationSetTheoryList)
    value = (value * 31) ^ hash(self.communicationsList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Digest(object):
  """
  Analytic-specific information about an attribute or edge. Digests
  are used to combine information from multiple sources to generate a
  unified value. The digests generated by an analytic will only ever
  be used by that same analytic, so analytics can feel free to encode
  information in whatever way is convenient.

  Attributes:
   - bytesValue: The following fields define various ways you can store the
  digest data (for convenience). If none of these meets your
  needs, then serialize the digest to a byte sequence and store it
  in bytesValue.
   - int64Value
   - doubleValue
   - stringValue
   - int64List
   - doubleList
   - stringList
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'bytesValue', None, None, ), # 1
    (2, TType.I64, 'int64Value', None, None, ), # 2
    (3, TType.DOUBLE, 'doubleValue', None, None, ), # 3
    (4, TType.STRING, 'stringValue', None, None, ), # 4
    (5, TType.LIST, 'int64List', (TType.I64,None), None, ), # 5
    (6, TType.LIST, 'doubleList', (TType.DOUBLE,None), None, ), # 6
    (7, TType.LIST, 'stringList', (TType.STRING,None), None, ), # 7
  )

  def __init__(self, bytesValue=None, int64Value=None, doubleValue=None, stringValue=None, int64List=None, doubleList=None, stringList=None,):
    self.bytesValue = bytesValue
    self.int64Value = int64Value
    self.doubleValue = doubleValue
    self.stringValue = stringValue
    self.int64List = int64List
    self.doubleList = doubleList
    self.stringList = stringList

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
        if ftype == TType.STRING:
          self.bytesValue = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.int64Value = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.DOUBLE:
          self.doubleValue = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.stringValue = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.int64List = []
          (_etype108, _size105) = iprot.readListBegin()
          for _i109 in xrange(_size105):
            _elem110 = iprot.readI64();
            self.int64List.append(_elem110)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.doubleList = []
          (_etype114, _size111) = iprot.readListBegin()
          for _i115 in xrange(_size111):
            _elem116 = iprot.readDouble();
            self.doubleList.append(_elem116)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.stringList = []
          (_etype120, _size117) = iprot.readListBegin()
          for _i121 in xrange(_size117):
            _elem122 = iprot.readString().decode('utf-8')
            self.stringList.append(_elem122)
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
    oprot.writeStructBegin('Digest')
    if self.bytesValue is not None:
      oprot.writeFieldBegin('bytesValue', TType.STRING, 1)
      oprot.writeString(self.bytesValue)
      oprot.writeFieldEnd()
    if self.int64Value is not None:
      oprot.writeFieldBegin('int64Value', TType.I64, 2)
      oprot.writeI64(self.int64Value)
      oprot.writeFieldEnd()
    if self.doubleValue is not None:
      oprot.writeFieldBegin('doubleValue', TType.DOUBLE, 3)
      oprot.writeDouble(self.doubleValue)
      oprot.writeFieldEnd()
    if self.stringValue is not None:
      oprot.writeFieldBegin('stringValue', TType.STRING, 4)
      oprot.writeString(self.stringValue.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.int64List is not None:
      oprot.writeFieldBegin('int64List', TType.LIST, 5)
      oprot.writeListBegin(TType.I64, len(self.int64List))
      for iter123 in self.int64List:
        oprot.writeI64(iter123)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.doubleList is not None:
      oprot.writeFieldBegin('doubleList', TType.LIST, 6)
      oprot.writeListBegin(TType.DOUBLE, len(self.doubleList))
      for iter124 in self.doubleList:
        oprot.writeDouble(iter124)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.stringList is not None:
      oprot.writeFieldBegin('stringList', TType.LIST, 7)
      oprot.writeListBegin(TType.STRING, len(self.stringList))
      for iter125 in self.stringList:
        oprot.writeString(iter125.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.bytesValue)
    value = (value * 31) ^ hash(self.int64Value)
    value = (value * 31) ^ hash(self.doubleValue)
    value = (value * 31) ^ hash(self.stringValue)
    value = (value * 31) ^ hash(self.int64List)
    value = (value * 31) ^ hash(self.doubleList)
    value = (value * 31) ^ hash(self.stringList)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AnnotationMetadata(object):
  """
  Metadata associated with an annotation or a set of annotations,
  that identifies where those annotations came from.

  Attributes:
   - tool: The name of the tool that generated this annotation.
   - timestamp: The time at which this annotation was generated (in unix time
  UTC -- i.e., seconds since January 1, 1970).
   - digest: A Digest, carrying over any information the annotation metadata
  wishes to carry over.
   - dependencies: The theories that supported this annotation.

  An empty field indicates that the theory has no
  dependencies (e.g., an ingester).
   - kBest: An integer that represents a ranking for systems
  that output k-best lists.

  For systems that do not output k-best lists,
  the default value (1) should suffice.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'tool', None, None, ), # 1
    (2, TType.I64, 'timestamp', None, None, ), # 2
    None, # 3
    (4, TType.STRUCT, 'digest', (Digest, Digest.thrift_spec), None, ), # 4
    (5, TType.STRUCT, 'dependencies', (TheoryDependencies, TheoryDependencies.thrift_spec), None, ), # 5
    (6, TType.I32, 'kBest', None, 1, ), # 6
  )

  def __init__(self, tool=None, timestamp=None, digest=None, dependencies=None, kBest=thrift_spec[6][4],):
    self.tool = tool
    self.timestamp = timestamp
    self.digest = digest
    self.dependencies = dependencies
    self.kBest = kBest

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
        if ftype == TType.STRING:
          self.tool = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.timestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.digest = Digest()
          self.digest.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.dependencies = TheoryDependencies()
          self.dependencies.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.kBest = iprot.readI32();
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
    oprot.writeStructBegin('AnnotationMetadata')
    if self.tool is not None:
      oprot.writeFieldBegin('tool', TType.STRING, 1)
      oprot.writeString(self.tool.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.timestamp is not None:
      oprot.writeFieldBegin('timestamp', TType.I64, 2)
      oprot.writeI64(self.timestamp)
      oprot.writeFieldEnd()
    if self.digest is not None:
      oprot.writeFieldBegin('digest', TType.STRUCT, 4)
      self.digest.write(oprot)
      oprot.writeFieldEnd()
    if self.dependencies is not None:
      oprot.writeFieldBegin('dependencies', TType.STRUCT, 5)
      self.dependencies.write(oprot)
      oprot.writeFieldEnd()
    if self.kBest is not None:
      oprot.writeFieldBegin('kBest', TType.I32, 6)
      oprot.writeI32(self.kBest)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.tool is None:
      raise TProtocol.TProtocolException(message='Required field tool is unset!')
    if self.timestamp is None:
      raise TProtocol.TProtocolException(message='Required field timestamp is unset!')
    if self.kBest is None:
      raise TProtocol.TProtocolException(message='Required field kBest is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tool)
    value = (value * 31) ^ hash(self.timestamp)
    value = (value * 31) ^ hash(self.digest)
    value = (value * 31) ^ hash(self.dependencies)
    value = (value * 31) ^ hash(self.kBest)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class CommunicationMetadata(object):
  """
  Metadata specific to a particular Communication object.
  This might include corpus-specific metadata (from the Twitter API),
  attributes associated with the Communication (the author),
  or other information about the Communication.

  Attributes:
   - tweetInfo: Extra information for communications where kind==TWEET:
  Information about this tweet that is provided by the Twitter
  API.  For information about the Twitter API, see:
  <https://dev.twitter.com/docs/platform-objects>
   - emailInfo: Extra information for communications where kind==EMAIL
   - nitfInfo: Extra information that may come from the NITF
  (News Industry Text Format) schema. See 'nitf.thrift'.
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'tweetInfo', (concrete.twitter.ttypes.TweetInfo, concrete.twitter.ttypes.TweetInfo.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'emailInfo', (concrete.email.ttypes.EmailCommunicationInfo, concrete.email.ttypes.EmailCommunicationInfo.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'nitfInfo', (concrete.nitf.ttypes.NITFInfo, concrete.nitf.ttypes.NITFInfo.thrift_spec), None, ), # 3
  )

  def __init__(self, tweetInfo=None, emailInfo=None, nitfInfo=None,):
    self.tweetInfo = tweetInfo
    self.emailInfo = emailInfo
    self.nitfInfo = nitfInfo

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
          self.tweetInfo = concrete.twitter.ttypes.TweetInfo()
          self.tweetInfo.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.emailInfo = concrete.email.ttypes.EmailCommunicationInfo()
          self.emailInfo.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.nitfInfo = concrete.nitf.ttypes.NITFInfo()
          self.nitfInfo.read(iprot)
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
    oprot.writeStructBegin('CommunicationMetadata')
    if self.tweetInfo is not None:
      oprot.writeFieldBegin('tweetInfo', TType.STRUCT, 1)
      self.tweetInfo.write(oprot)
      oprot.writeFieldEnd()
    if self.emailInfo is not None:
      oprot.writeFieldBegin('emailInfo', TType.STRUCT, 2)
      self.emailInfo.write(oprot)
      oprot.writeFieldEnd()
    if self.nitfInfo is not None:
      oprot.writeFieldBegin('nitfInfo', TType.STRUCT, 3)
      self.nitfInfo.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tweetInfo)
    value = (value * 31) ^ hash(self.emailInfo)
    value = (value * 31) ^ hash(self.nitfInfo)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
