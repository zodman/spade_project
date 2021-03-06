import spade
import time
import sys
import terminal as t
from terminal import log
import json

host = "127.0.0.1"

class Client(spade.Agent.Agent):
    default_location = "yucatan"
    index = {'yucatan':range(1,999)}

    def _setup(self):
        data = self.data

        if len(data) > 3:
            small_data = data[-3:]
            try:
                data_int = "%s"  % int(small_data)
            except Exception as e:
                log.error("%s no encontrado" % data)
                return
        else:
            data_int =  self.data
        if self.action == "search":
            for key,value in self.index.items():
                if data_int in value:
                    self.default_location= key
                    break
        log.info("ask to %s" % self.default_location)
        template = spade.Behaviour.ACLTemplate()
        template.setSender(spade.AID.aid(self.default_location+"@"+host,["xmpp://"+self.default_location+"@"+host]))
        t = spade.Behaviour.MessageTemplate(template)

        #self.runBehaviourOnce(self.CheckBehav())
        self.addBehaviour(self.ReciveBehav(), t)
        self.addBehaviour(self.SendMsgBehav())

    #class CheckBehav(spade.Behaviour.OneShotBehaviour):
        #def _process(self):
            #print "check beahv"
            #aad = spade.AMS.AmsAgentDescription()
            #search = self.myAgent.searchAgent(aad)
            #log.info("saerch %s" % search)
            #for a in search:
                #print a.asRDFXML()



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
            msg.addReceiver(spade.AID.aid("%s@%s" % (self.myAgent.default_location, host),
                 ["xmpp://%s@%s" %(self.myAgent.default_location, host)]))
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
    if action =="search":
        data = t.prompt("%s for NS:"% action)
    else:
        data = t.prompt("%s for id:"% action)
    a.data = data
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
