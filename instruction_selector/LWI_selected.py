from format_validator import FormatValidator
from I_instructions.LWI import LWI

def LWISelected(instruction: list[str]) -> str:
  if FormatValidator.validateLWI(instruction):
    rd = int(instruction[1])
    lit16 = int(instruction[2])
    lwi = LWI(rd, lit16)
    return lwi.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."