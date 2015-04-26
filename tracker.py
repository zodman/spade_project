import spade

class Tracker(spade.Agent.Agent):
    class MyBehav(spade.Behaviour.PeriodicBehaviour):

        def _onTick(self):
            print "I'm going to search for an agent"
            aad = spade.AMS.AmsAgentDescription()
            search = self.myAgent.searchAgent(aad)
            print search
            
        def onStart(self):
            print "tracker start"

    def _setup(self):
        print "%s starting . . ." % self.__class__.__name__
        b = self.MyBehav(100)
        self.addBehaviour(b, None)

if __name__ == "__main__":
    a = Tracker("tracker@127.0.0.1", "secret")
    a.start()