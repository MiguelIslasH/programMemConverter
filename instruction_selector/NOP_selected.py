from validation.format_validator_other import FormatValidatorOther
from other_instructions.NOP import NOP

def NOPSelected(instruction: list[str]) -> str:
  if FormatValidatorOther.validateNOP(instruction):
    nop = NOP()
    return nop.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."