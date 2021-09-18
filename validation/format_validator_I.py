class FormatValidator:
  def __init__(self):
    pass

  def validateLI(LIInstructions: list[str]) -> bool:
    rd = LIInstructions[1]
    lit16 = LIInstructions[2]
    if len(LIInstructions) > 3:
      return False

    if len(LIInstructions) < 3:
      return False
      
    try:
      int(rd)
      int(lit16)
      return True
    except:
      return False

  def validateLWI(LWIInstructions: list[str]) -> bool:
    rd = LWIInstructions[1]
    lit16 = LWIInstructions[2]
    if len(LWIInstructions) > 3:
      return False

    if len(LWIInstructions) < 3:
      return False
      
    try:
      int(rd)
      int(lit16)
      return True
    except:
      return False
  
  def validateLW(LWInstructions: list[str]) -> bool:
    rd = LWInstructions[1]
    rt = LWInstructions[2]
    lit12 = LWInstructions[3]
    if len(LWInstructions) > 4:
      return False
      
    if len(LWInstructions) < 4:
      return False

    try:
      int(rd)
      int(rt)
      int(lit12)
      return True
    except:
      return False

  def validateSWI(SWIInstructions: list[str]) -> bool:
    rd = SWIInstructions[1]
    lit16 = SWIInstructions[2]
    if len(SWIInstructions) > 3:
      return False
      
    if len(SWIInstructions) < 3:
      return False

    try:
      int(rd)
      int(lit16)
      return True
    except:
      return False

  def validateSW(SWInstructions: list[str]) -> bool:
    rd = SWInstructions[1]
    rt = SWInstructions[2]
    lit12 = SWInstructions[3]
    if len(SWInstructions) > 4:
      return False
      
    if len(SWInstructions) < 4:
      return False

    try:
      int(rd)
      int(rt)
      int(lit12)
      return True
    except:
      return False

  def validateBLETI(BLETInstructions: list[str]) -> bool:
    rd = BLETInstructions[1]
    rt = BLETInstructions[2]
    lit12 = BLETInstructions[3]
    if len(BLETInstructions) > 4:
      return False
      
    if len(BLETInstructions) < 4:
      return False

    try:
      int(rd)
      int(rt)
      int(lit12)
      return True
    except:
      return False

  def validateBLTI(BLTInstructions: list[str]) -> bool:
    try:
      rd = BLTInstructions[1]
      rt = BLTInstructions[2]
      lit12 = BLTInstructions[3]
      if len(BLTInstructions) > 4:
        return False
        
      if len(BLTInstructions) < 4:
        return False

      int(rd)
      int(rt)
      int(lit12)
      return True
    except:
      return False

  def validateADDI(ADDIInstructions: list[str]) -> bool:
    rd = ADDIInstructions[1]
    rt = ADDIInstructions[2]
    lit12 = ADDIInstructions[3]
    if len(ADDIInstructions) > 4:
      return False
      
    if len(ADDIInstructions) < 4:
      return False

    try:
      int(rd)
      int(rt)
      int(lit12)
      return True
    except:
      return False