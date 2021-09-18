from validation.format_validator_R import FormatValidatorR
from R_instructions.ADD import ADD

def ADDSelected(instruction: list[str]) -> str:
  if FormatValidatorR.validateADD(instruction):
    rd = int(instruction[1])
    rt = int(instruction[2])
    rs = int(instruction[3])
    add = ADD(rd, rt, rs)
    return add.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."