class ADD:
  opCodeBits = ""
  rdBits = ""
  rtBits = ""
  rsBits = ""

  def convertToBits(self):
    self.opCodeBits =  '{0:05b}'.format(self.opCode)
    self.rdBits = '{0:04b}'.format(self.Rd)
    self.rtBits = '{0:04b}'.format(self.Rt)
    self.rsBits = '{0:04b}'.format(self.Rs)

  def __init__(self, Rd, Rt, Rs):
    self.opCode = 0
    self.format = "R"
    self.Rd = Rd
    self.Rt = Rt
    self.Rs = Rs
    self.convertToBits()

  def showProgramMem(self) -> str:
    print("Op code | Rd | Rt | Rs | S/U | 0000 -> Format:", self.format)
    return str(
      self.opCodeBits + " | " + self.rdBits + " | "
       + self.rtBits + " | " + self.rsBits + " | " + "0000" + " | " + "0000"
       )