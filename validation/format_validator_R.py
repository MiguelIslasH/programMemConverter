class FormatValidatorR:
  def validateADD(ADDInstructions: list[str]):
    rd = ADDInstructions[1]
    rt = ADDInstructions[2]
    rs = ADDInstructions[3]

    if len(ADDInstructions) > 4:
      return False
    
    if len(ADDInstructions) < 4:
      return False
    
    try:
      int(rd)
      int(rt)
      int(rs)
      return True
    except:
      return False

  def validateSRL(SRLInstructions: list[str]):
    rd = SRLInstructions[1]
    rt = SRLInstructions[2]
    lit4 = SRLInstructions[3]

    if len(SRLInstructions) > 4:
      return False
    
    if len(SRLInstructions) < 4:
      return False
    
    try:
      int(rd)
      int(rt)
      int(lit4)
      return True
    except:
      return False