import os
import sys
import time

import spade

import pprint
import json

host = "127.0.0.1"

class Sender(spade.Agent.Agent):

		
    class SendMsgBehav(spade.Behaviour.OneShotBehaviour):
        """
        This behaviour sends a message to this same agent to trigger an EventBehaviour
        """

        def _process(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("inform")
            msg.addReceiver(spade.AID.aid("a@"+host,["xmpp://a@"+host]))
            data = {'data':'data1', 'num':1}
            msg.setContent(data)
            print "Sending message in 1 . . ."
            time.sleep(1)

            self.myAgent.send(msg)
            
            print "I sent a message"
            #print str(msg)
    
    class RecvMsgBehav(spade.Behaviour.EventBehaviour):
        """
        This EventBehaviour gets launched when a message that matches its template arrives at the agent
        """

        def _process(self):            
            print "This behaviour has been triggered by a message!"
            self.msg = self._receive(True, 10)
            # Check wether the message arrived
            if self.msg is not None:
                print "I got a message!"
                print (self.msg.getContent(),)
            else:
                print "I waited but got no message"
            
    
    def _setup(self):
        # Create the template for the EventBehaviour: a message from myself
        template = spade.Behaviour.ACLTemplate()
        template.setSender(spade.AID.aid("a@"+host,["xmpp://a@"+host]))
        t = spade.Behaviour.MessageTemplate(template)
        
        # Add the EventBehaviour with its template
        self.addBehaviour(self.RecvMsgBehav(),t)
        
        # Add the sender behaviour
        self.addBehaviour(self.SendMsgBehav())

    
a = Sender("a@"+host,"secret")

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
