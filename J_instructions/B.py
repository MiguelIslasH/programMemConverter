from utils.functions import Functions

class B:
  opCodeBits = ""
  lit16Bits = "0000000000000000"

  def convertToBits(self):
    self.opCodeBits =  '{0:05b}'.format(self.opCode)
    self.lit16Bits = '{0:016b}'.format(self.lit16)

  def __init__(self, lit16: int):
    self.opCode = 19
    self.format = "J"
    self.lit16 = lit16
    self.convertToBits()

  def showProgramMem(self) -> str:
    print("Op code | S/U | lit16 -> Format:", self.format)
    return str(
      self.opCodeBits + " | " + "0000" + " | "
       + Functions.spacesBetweenBits(self.lit16Bits, 4)
       )