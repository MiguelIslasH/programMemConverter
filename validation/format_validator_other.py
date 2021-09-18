class FormatValidatorOther:
  def validateNOP(NOPInstructions: list[str]):
    if len(NOPInstructions) > 1:
      return False
    
    if len(NOPInstructions) < 1:
      return False
    
    return True

  def validateRET(RETInstructions: list[str]):
    if len(RETInstructions) > 1:
      return False
    
    if len(RETInstructions) < 1:
      return False
    
    return True