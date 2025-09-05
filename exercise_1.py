class InputGuardRailTripwireTriggered(Exception):
    pass

class Agent:
    def respond(self, user_input: str):
        try:
            if "😭" in user_input:
                raise InputGuardRailTripwireTriggered("Emoji not allowed in input!")

            return f"Agent Response: {user_input}"

        except InputGuardRailTripwireTriggered as e:
            print(f"[LOG] InputGuardRailTripwireTriggered: {e}")

if __name__ == "__main__":
    agent = Agent()
    prompt = "I want to change my class timings 😭😭"
    print("User:", prompt)
    response = agent.respond(prompt)
    print("Response:", response)
