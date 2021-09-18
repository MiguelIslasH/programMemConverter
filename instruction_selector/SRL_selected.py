from validation.format_validator_R import FormatValidatorR
from R_instructions.SRL import SRL

def SRLSelected(instruction: list[str]) -> str:
  if FormatValidatorR.validateSRL(instruction):
    rd = int(instruction[1])
    rt = int(instruction[2])
    lit4 = int(instruction[3])
    srl = SRL(rd, rt, lit4)
    return srl.showProgramMem()
  else:
    return "No valid format for " + instruction[0].upper() + " instruction."