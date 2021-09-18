from validation.format_validator_I import FormatValidator
from I_instructions.SWI import SWI

def SWISelected(instruction: list[str]) -> str:
  if FormatValidator.validateSWI(instruction):
    rd = int(instruction[1])
    lit16 = int(instruction[2])
    swi = SWI(rd, lit16)
    return swi.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."