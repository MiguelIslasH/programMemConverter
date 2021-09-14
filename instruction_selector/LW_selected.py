from validation.format_validator import FormatValidator
from I_instructions.LW import LW

def LWSelected(instruction: list[str]) -> str:
  if FormatValidator.validateLW(instruction):
    rd = int(instruction[1])
    rt = int(instruction[2])
    lit12 = int(instruction[3])
    lw = LW(rd, rt, lit12)
    return lw.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."