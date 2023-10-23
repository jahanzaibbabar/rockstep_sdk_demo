
class RockStepAuth:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_headers(self):
        return {"Authorization": f"Bearer {self.api_key}"}
