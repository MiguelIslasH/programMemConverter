class NOP:
  opCodeBits = ""
  rdBits = "0000"

  def convertToBits(self):
    self.opCodeBits =  '{0:05b}'.format(self.opCode)

  def __init__(self):
    self.opCode = 22
    self.format = "Other"
    self.convertToBits()

  def showProgramMem(self) -> str:
    print("Op code | S/U | S/U | S/U | S/U | S/U -> Format:", self.format)
    return str(
      self.opCodeBits + " | " + "0000" + " | "
       + "0000" + " | " + "0000" + " | " + "0000" + " | " + "0000"
       )