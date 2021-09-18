from validation.format_validator_other import FormatValidatorOther
from other_instructions.RET import RET

def RETSelected(instruction: list[str]) -> str:
  if FormatValidatorOther.validateRET(instruction):
    ret = RET()
    return ret.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."