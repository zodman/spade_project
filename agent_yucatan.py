import spade
import time
import sys
import json
from action import Action
import terminal as t

host = "127.0.0.1"

class AgentBase(spade.Agent.Agent):
    class ReciveBehav(spade.Behaviour.EventBehaviour):
        def _process(self):
            self.msg = self._receive(True, 10)
            content = None
            if self.msg is not None:
                t.log.info("msg recived")
                content = self.msg.getContent()
                t.log.info(content)
                act = Action(content)
                res  = act.execute()
    def _setup(self):
        template = spade.Behaviour.ACLTemplate()
        template.setSender(spade.AID.aid("client@"+host,["xmpp://client@"+host]))
        t = spade.Behaviour.MessageTemplate(template)
        
        self.addBehaviour(self.ReciveBehav(), t)

app = t.Command("main")
app.option("-d", "debug")

@app.action
def main(debug=False):
    a = AgentBase("yucatan@"+host,"secret")
    if debug:
        a.setDebug()

    time.sleep(1)

    a.start()

    alive = True
    while alive:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            alive=False
    a.stop()
    sys.exit(0)

app.parse()
