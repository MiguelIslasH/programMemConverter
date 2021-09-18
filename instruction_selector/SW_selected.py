from validation.format_validator_I import FormatValidator
from I_instructions.SW import SW

def SWSelected(instruction: list[str]) -> str:
  if FormatValidator.validateSW(instruction):
    rd = int(instruction[1])
    rt = int(instruction[2])
    lit12 = int(instruction[3])
    sw = SW(rd, rt, lit12)
    return sw.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."