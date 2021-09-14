class LW:
  opCodeBits = ""
  rdBits = ""
  lit16Bits = ""
  rtBits = ""

  def convertToBits(self):
    self.opCodeBits =  '{0:05b}'.format(self.opCode)
    self.rdBits =  '{0:04b}'.format(self.Rd)
    self.rtBits =  '{0:04b}'.format(self.Rt)
    self.lit16Bits = '{0:012b}'.format(self.lit12)

  def __init__(self, Rd: int, lit12: int, Rt: int):
    self.Rd = Rd
    self.Rt = Rt
    self.lit12 = lit12
    self.opCode = 23
    self.format = "I"
    self.convertToBits()

  def showProgramMem(self) -> str:
    print("Op code | Rd | Rt | lit12 -> Format:", self.format)
    return str(
      self.opCodeBits + " | " + self.rdBits + " | "
       + self.rtBits + " | " + self.lit16Bits
       )