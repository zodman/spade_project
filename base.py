import spade


class Base(spade.Agent.Agent):

    class InformBehav(spade.Behaviour.OneShotBehaviour):

        def _process(self):
            # First, form the receiver AID
            receiver = spade.AID.aid(name="receiver@127.0.0.1",
                                     addresses=["xmpp://receiver@127.0.0.1"])

            # Second, build the message
            self.msg = spade.ACLMessage.ACLMessage()  # Instantiate the message
            # Set the "inform" FIPA performative
            self.msg.setPerformative("inform")
            # Set the ontology of the message content
            self.msg.setOntology("myOntology")
            # Set the language of the message content
            self.msg.setLanguage("OWL-S")
            # Add the message receiver
            self.msg.addReceiver(receiver)
            self.msg.setContent("Hello World")        # Set the message content

            # Third, send the message with the "send" method of the agent
            self.myAgent.send(self.msg)

    def _setup(self):
        print "MyAgent starting . . ."
        b = self.InformBehav()
        self.addBehaviour(b, None)

if __name__ == "__main__":
    a = Base("agent@127.0.0.1", "secret")
    a.start()

