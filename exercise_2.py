class FatherGuardrailsTriggered(Exception):
    pass

class FatherAgent:
    def check_temperature(self,temp:int):
      try:
        if temp < 26:
           raise FatherGuardrailsTriggered("Father: No, you cannot go out under 26C!")
        return f"Father: Okay, you can go out at {temp}C."
      
      except FatherGuardrailsTriggered as e:
            print(f"[LOG] FatherGuardRailTriggered: {e}")

if __name__ == "__main__":
    father = FatherAgent()
    temp = 24  # test input
    print("Child: I want to go out!")
    response = father.check_temperature(temp)
    print("Response:", response)
