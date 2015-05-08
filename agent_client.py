import spade
import time
import sys
import terminal as t
from terminal import log
import json

host = "127.0.0.1"

class Client(spade.Agent.Agent):
    def _setup(self):
        self.addBehaviour(self.SendMsgBehav())
        
        template = spade.Behaviour.ACLTemplate()
        template.setSender(spade.AID.aid("yucatan@"+host,["xmpp://yucatan@"+host]))
        t = spade.Behaviour.MessageTemplate(template)
        
        self.addBehaviour(self.ReciveBehav(), t)


    class ReciveBehav(spade.Behaviour.EventBehaviour):
        def _process(self):
            self.msg = self._receive(True, 10)
            content = None
            if self.msg is not None:
                log.info("msg arrived")
                json_str = self.msg.getContent()
                log.info((json_str,))
                msg_replied = json.loads(json_str.replace("'","\"").replace("u\"","\""))
                for i in msg_replied.get("data").split("\n"):
                    log.info(t.blue(i))

		
    class SendMsgBehav(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("inform")
            msg.addReceiver(spade.AID.aid("yucatan@"+host,["xmpp://yucatan@"+host]))
            #data = {'data':'Andres Vargas', 'action':"search"}
            data = {'data':self.myAgent.data, 'action':self.myAgent.action}
            msg.setContent(data)
            log.info("Sending message in 1 . . .")
            time.sleep(1)
            self.myAgent.send(msg)
            log.info(t.blue("I sent a message"))

app = t.Command("client")
app.option("-d", "debug")
app.option("-a [action]", "action: search|fetch",)

@app.action
def main(debug = False, action="search"):

    a = Client("client@"+host,"secret")
    a.action = action
    if debug:
        a.setDebug()
    data = t.prompt("%s for"% action)
    a.data = data
    time.sleep(1)
    a.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    a.stop()


    sys.exit(0)

app.parse()
