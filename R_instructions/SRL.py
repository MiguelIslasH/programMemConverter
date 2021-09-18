class SRL:
  opCodeBits = ""
  rdBits = ""
  rtBits = ""
  lit4Bits = ""

  def convertToBits(self):
    self.opCodeBits =  '{0:05b}'.format(self.opCode)
    self.rdBits = '{0:04b}'.format(self.Rd)
    self.rtBits = '{0:04b}'.format(self.Rt)
    self.lit4Bits = '{0:04b}'.format(self.lit4)

  def __init__(self, Rd, Rt, lit4):
    self.opCode = 0
    self.format = "R"
    self.Rd = Rd
    self.Rt = Rt
    self.lit4 = lit4
    self.convertToBits()

  def showProgramMem(self) -> str:
    print("Op code | Rd | Rt | S/U | lit4 | 0010 -> Format:", self.format)
    return str(
      self.opCodeBits + " | " + self.rdBits + " | "
       + self.rtBits + " | " + "0000" + " | " +self.lit4Bits + " | " + "0010"
       )