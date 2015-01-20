#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class Sound(object):
  """
  A sound wave. A separate optional field is defined for each
  suppported format. Typically, a Sound object will only define
  a single field.

  Note: we may want to have separate fields for separate channels
  (left vs right), etc.

  Attributes:
   - wav
   - mp3
   - sph
   - path: An absolute path to a file on disk where the sound file can be
  found. It is assumed that this path will be accessable from any
  machine that the system is run on (i.e., it should be a shared
  disk, or possibly a mirrored directory).
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'wav', None, None, ), # 1
    (2, TType.STRING, 'mp3', None, None, ), # 2
    (3, TType.STRING, 'sph', None, None, ), # 3
    (4, TType.STRING, 'path', None, None, ), # 4
  )

  def __init__(self, wav=None, mp3=None, sph=None, path=None,):
    self.wav = wav
    self.mp3 = mp3
    self.sph = sph
    self.path = path

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
          self.wav = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.mp3 = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.sph = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.path = iprot.readString().decode('utf-8')
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
    oprot.writeStructBegin('Sound')
    if self.wav is not None:
      oprot.writeFieldBegin('wav', TType.STRING, 1)
      oprot.writeString(self.wav)
      oprot.writeFieldEnd()
    if self.mp3 is not None:
      oprot.writeFieldBegin('mp3', TType.STRING, 2)
      oprot.writeString(self.mp3)
      oprot.writeFieldEnd()
    if self.sph is not None:
      oprot.writeFieldBegin('sph', TType.STRING, 3)
      oprot.writeString(self.sph)
      oprot.writeFieldEnd()
    if self.path is not None:
      oprot.writeFieldBegin('path', TType.STRING, 4)
      oprot.writeString(self.path.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.wav)
    value = (value * 31) ^ hash(self.mp3)
    value = (value * 31) ^ hash(self.sph)
    value = (value * 31) ^ hash(self.path)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
