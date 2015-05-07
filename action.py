import json
import peewee
import os

from util.model import Person
import terminal  as t

class Action:
    def __init__(self, json_str):
        self.json = json.loads(json_str.replace("'","\""))

    def execute(self):
        action = self.json.get("action")
        data = self.json.get("data")
        if action == "search":
            t.log.info("pre-exec search")
            self.search(data)
        elif action == "fetch":
            t.log.info("pre-exec fetch")
            self.fetch(data)
        else:
            t.log.erro("not action found")

    def search(self, data):
        t.log.info("searching")
        persons = Person.select().where(Person.name.contains(data))
        for person in persons:
            t.log.info("id:%s %s %s" %(person.id, person.name, 
                        person.social_number))

    def fetch(self, id):
        person = Person.get(Person.id==int(id))
        t.log.info(t.red("person"))
        t.log.info(" %s NS: %s Nombre %s" % (person.id, 
                person.social_number, person.name))

