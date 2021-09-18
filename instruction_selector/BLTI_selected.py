from validation.format_validator_I import FormatValidator
from I_instructions.BLTI import BLTI

def BLTISelected(instruction: list[str]) -> str:
  if FormatValidator.validateBLTI(instruction):
    rd = int(instruction[1])
    rt = int(instruction[2])
    lit12 = int(instruction[3])
    blti = BLTI(rd, rt, lit12)
    return blti.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."