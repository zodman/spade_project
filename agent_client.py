import spade
import time
import sys
host = "127.0.0.1"

class Client(spade.Agent.Agent):
    def _setup(self):
        self.addBehaviour(self.SendMsgBehav())
		
    class SendMsgBehav(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("inform")
            msg.addReceiver(spade.AID.aid("yucatan@"+host,["xmpp://yucatan@"+host]))
            data = {'data':'data1', 'num':1}
            msg.setContent(data)
            print "Sending message in 1 . . ."
            time.sleep(1)
            self.myAgent.send(msg)
            
            print "I sent a message"

a = Client("client@"+host,"secret")

time.sleep(1)
a.start()

alive = True
import time
while alive:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        alive=False
a.stop()
sys.exit(0)

