from validation.format_validator_I import FormatValidator
from I_instructions.BLETI import BLETI

def BLETISelected(instruction: list[str]) -> str:
  if FormatValidator.validateBLETI(instruction):
    rd = int(instruction[1])
    rt = int(instruction[2])
    lit12 = int(instruction[3])
    bleti = BLETI(rd, rt, lit12)
    return bleti.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."