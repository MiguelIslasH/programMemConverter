from validation.format_validator_J import FormatValidatorJ
from J_instructions.B import B

def BSelected(instruction: list[str]) -> str:
  if FormatValidatorJ.validateB(instruction):
    lit16 = int(instruction[1])
    b = B(lit16)
    return b.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."