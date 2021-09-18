class FormatValidatorJ:
  def validateB(BInstructions: list[str]):
    lit16 = BInstructions[1]
    if len(BInstructions) > 2:
      return False
    
    if len(BInstructions) < 2:
      return False
    
    try:
      int(lit16)
      return True
    except:
      return False

  def validateCALL(CALLInstructions: list[str]):
    lit16 = CALLInstructions[1]
    if len(CALLInstructions) > 2:
      return False
    
    if len(CALLInstructions) < 2:
      return False
    
    try:
      int(lit16)
      return True
    except:
      return False