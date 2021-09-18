from validation.format_validator_I import FormatValidator
from I_instructions.ADDI import ADDI

def ADDISelected(instruction: list[str]) -> str:
  if FormatValidator.validateADDI(instruction):
    rd = int(instruction[1])
    rt = int(instruction[2])
    lit12 = int(instruction[3])
    addi = ADDI(rd, rt, lit12)
    return addi.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."