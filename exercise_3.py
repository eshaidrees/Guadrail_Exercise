class GateKeeperGuardRailTriggered(Exception):
    pass

class GateKeeper:
    def allow_entry(self,school_name:str):
        try:
            if school_name != "MySchool":
                raise GateKeeperGuardRailTriggered("GateKeeper: Only MySchool students allowed!")

            return f"GateKeeper: Welcome, {school_name} student."

        except GateKeeperGuardRailTriggered as e:
            print(f"[LOG] GateKeeperGuardRailTriggered: {e}")

if __name__ == "__main__":
    gatekeeper = GateKeeper()
    school_name = "Other School"  # test input
    print(f"Student from {school_name} Can i enter?")
    response = gatekeeper.allow_entry(school_name)
    print("Response:", response)
