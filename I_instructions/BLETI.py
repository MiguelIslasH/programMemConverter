from utils.functions import Functions

class BLETI:
  opCodeBits = ""
  rdBits = ""
  rtBits = ""
  lit12Bits = ""

  def convertToBits(self):
    self.opCodeBits = '{0:05b}'.format(self.opCode)
    self.rdBits = '{0:04b}'.format(self.Rd)
    self.rtBits = '{0:04b}'.format(self.Rt)
    self.lit12Bits = '{0:012b}'.format(self.lit12)

  def __init__(self, Rd: int, Rt: int, lit12: int):
    self.Rd = Rd
    self.Rt = Rt
    self.lit12 = lit12
    self.opCode = 16
    self.format = "I"
    self.convertToBits()

  def showProgramMem(self) -> str:
    print("Op code | Rd | Rt | lit12 -> Format:", self.format)
    return str(
      self.opCodeBits + " | " + self.rdBits + " | " + self.rtBits + " | "
       + Functions.spacesBetweenBits(self.lit12Bits, 4)
       )