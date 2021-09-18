from utils.functions import Functions

class SWI:
  opCodeBits = ""
  rdBits = ""
  lit16Bits = ""

  def convertToBits(self):
    self.opCodeBits =  '{0:05b}'.format(self.opCode)
    self.rdBits =  '{0:04b}'.format(self.Rd)
    self.lit16Bits = '{0:016b}'.format(self.lit16)

  def __init__(self, Rd: int, lit16: int):
    self.Rd = Rd
    self.lit16 = lit16
    self.opCode = 3
    self.format = "I"
    self.convertToBits()

  def showProgramMem(self) -> str:
    print("Op code | Rd | lit16 -> Format:", self.format)
    return str(
      self.opCodeBits + " | " + self.rdBits + " | "
       + Functions.spacesBetweenBits(self.lit16Bits, 4)
       )