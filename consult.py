import spade
import time

class Client(spade.Agent.Agent):
    def _setup(self):
        self.addBehaviour(self.ClientBehav())

    class ClientBehav(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            pass

c = Client("client@127.0.0.1","secret")

c.start()
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        alive=False

c.stop()