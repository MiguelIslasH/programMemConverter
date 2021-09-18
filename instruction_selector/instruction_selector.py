from .LI_selected import LISelected
from .LWI_selected import LWISelected
from .LW_selected import LWSelected
from .BLETI_selected import BLETISelected
from .SWI_selected import SWISelected
from .ADDI_selected import ADDISelected
from .BLTI_selected import BLTISelected
from .SW_selected import SWSelected

from .B_selected import BSelected
from .CALL_selected import CALLSelected

from .NOP_selected import NOPSelected
from .RET_selected import RETSelected

from .ADD_selected import ADDSelected
from .SRL_selected import SRLSelected


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

  elif instruction[0].upper() == "BLETI":
    #Expected format: BLETI Rd Rt lit12
    print(BLETISelected(instruction))

  elif instruction[0].upper() == "SWI":
    #Expected format: SWI Rd lit16
    print(SWISelected(instruction))

  elif instruction[0].upper() == "SW":
    #Expected format: SW Rd Rt lit12 => SW Rd lit12(Rt)
    print(SWSelected(instruction))

  elif instruction[0].upper() == "NOP":
    #Expected format: NOP
    print(NOPSelected(instruction))

  elif instruction[0].upper() == "RET":
    #Expected format: RET
    print(RETSelected(instruction))

  elif instruction[0].upper() == "B":
    #Expected format: B lit16
    print(BSelected(instruction))

  elif instruction[0].upper() == "CALL":
    #Expected format: CALL lit16
    print(CALLSelected(instruction))

  elif instruction[0].upper() == "ADD":
    #Expected format: ADD Rd Rt Rs
    print(ADDSelected(instruction))

  elif instruction[0].upper() == "ADDI":
    #Expected format: ADDI Rd Rt lit12
    print(ADDISelected(instruction))

  elif instruction[0].upper() == "BLTI":
    #Expected format: BLTI Rd Rt lit12
    print(BLTISelected(instruction))

  elif instruction[0].upper() == "SRL":
    #Expected format: SRL Rd Rt lit4
    print(SRLSelected(instruction))
    
  else:
    return "No valid instruction"