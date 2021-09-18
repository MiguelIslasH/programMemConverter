from validation.format_validator_J import FormatValidatorJ
from J_instructions.CALL import CALL

def CALLSelected(instruction: list[str]) -> str:
  if FormatValidatorJ.validateCALL(instruction):
    lit16 = int(instruction[1])
    call = CALL(lit16)
    return call.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."