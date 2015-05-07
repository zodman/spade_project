import spade
import time
import sys
import terminal as t
from terminal import log

host = "127.0.0.1"

class Client(spade.Agent.Agent):
    def _setup(self):
        self.setDebug()
        self.addBehaviour(self.SendMsgBehav())
		
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
            self.myAgent.stop()
            
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
    sys.exit(0)

app.parse()
