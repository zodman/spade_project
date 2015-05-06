import json

class Action:
    def __init__(self, json_str):
        self.json = json.loads(json_str)

    def validate(self):
        assert "action" not in self.json, "No action"

    def execute(self):
        action = self.json.get("action")
        print "action ", action
        
