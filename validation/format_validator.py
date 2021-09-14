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