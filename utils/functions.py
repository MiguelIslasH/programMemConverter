class Functions:
  def spacesBetweenBits(string: str, length: int):
    return ' '.join(string[i:i+length] for i in range(0,len(string),length))
