# -*- coding: utf-8 -*-
#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings,coding=utf-8
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class TextSpan(object):
  """
  A span of text within a single communication, identified by a pair
  of zero-indexed character offsets into a Thrift string. Thrift strings
  are encoded using UTF-8:
    https://thrift.apache.org/docs/types
  The offsets are character-based, not byte-based - a character with a
  three-byte UTF-8 representation only counts as one character.

  NOTE: This span represents a best guess, or 'provenance':
  it cannot be guaranteed that this text span matches the _exact_
  text of the original document, but is the annotation's best
  effort at such a representation.

  Attributes:
   - start: Start character, inclusive.
   - ending: End character, exclusive
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'start', None, None, ), # 1
    (2, TType.I32, 'ending', None, None, ), # 2
  )

  def __init__(self, start=None, ending=None,):
    self.start = start
    self.ending = ending

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
        if ftype == TType.I32:
          self.start = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.ending = iprot.readI32()
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
    oprot.writeStructBegin('TextSpan')
    if self.start is not None:
      oprot.writeFieldBegin('start', TType.I32, 1)
      oprot.writeI32(self.start)
      oprot.writeFieldEnd()
    if self.ending is not None:
      oprot.writeFieldBegin('ending', TType.I32, 2)
      oprot.writeI32(self.ending)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.start is None:
      raise TProtocol.TProtocolException(message='Required field start is unset!')
    if self.ending is None:
      raise TProtocol.TProtocolException(message='Required field ending is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.start)
    value = (value * 31) ^ hash(self.ending)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AudioSpan(object):
  """
  A span of audio within a single communication, identified by a
  pair of time offests. Time offsets are zero-based.

  NOTE: This span represents a best guess, or 'provenance':
  it cannot be guaranteed that this text span matches the _exact_
  text of the original document, but is the annotation's best
  effort at such a representation.

  Attributes:
   - start: Start time (in seconds)
   - ending: End time (in seconds)
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'start', None, None, ), # 1
    (2, TType.I64, 'ending', None, None, ), # 2
  )

  def __init__(self, start=None, ending=None,):
    self.start = start
    self.ending = ending

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
        if ftype == TType.I64:
          self.start = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.ending = iprot.readI64()
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
    oprot.writeStructBegin('AudioSpan')
    if self.start is not None:
      oprot.writeFieldBegin('start', TType.I64, 1)
      oprot.writeI64(self.start)
      oprot.writeFieldEnd()
    if self.ending is not None:
      oprot.writeFieldBegin('ending', TType.I64, 2)
      oprot.writeI64(self.ending)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.start is None:
      raise TProtocol.TProtocolException(message='Required field start is unset!')
    if self.ending is None:
      raise TProtocol.TProtocolException(message='Required field ending is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.start)
    value = (value * 31) ^ hash(self.ending)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
