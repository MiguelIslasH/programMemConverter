from .LI_selected import LISelected
from .LWI_selected import LWISelected
from .LW_selected import LWSelected

def instructionSelector(instruction: str) -> str: 
  instruction = instruction.split(" ")

  if instruction[0].upper() == "LI":
    #Expected format: LI Rd Slit16
    print(LISelected(instruction))
  
  elif instruction[0].upper() == "LWI":
    #Expected format: LWI Rd lit16
    print(LWISelected(instruction))

  elif instruction[0].upper() == "LW":
    #Expected format: LW Rd Rt lit12
    print(LWSelected(instruction))
    
  else:
    return "No valid instruction"