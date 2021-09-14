from validation.format_validator import FormatValidator
from I_instructions.LI import LI

def LISelected(instruction: list[str]) -> str:
  if FormatValidator.validateLI(instruction):
    rd = int(instruction[1])
    lit16 = int(instruction[2])
    li = LI(rd, lit16)
    return li.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."