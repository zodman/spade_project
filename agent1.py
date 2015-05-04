import spade
import time
import sys

class AgentBase(spade.Agent.Agent):
    class ListenBehaviour(spade.Behaviour.EventBehaviour):
        def _process(self):
            self.msg = self._receive(True, 10)
            print (self.msg,self.msg.asJSON())
		



if __name__ == "__main__":
    time.sleep(1)
    a = AgentBase("a@127.0.0.1","secret")
    a.start()
    alive = True
    while alive:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            alive=False
    a.stop()
    sys.exit(0)
