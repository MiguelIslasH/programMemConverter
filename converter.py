from instruction_selector.instruction_selector import instructionSelector

if __name__ == "__main__":
  print("Convert Assembly instruction to program memory")
  while(True):
    print("\nType your instruction: \n")
    instruction = input("")
    if instruction == "q":
      break
    instructionSelector(instruction)
