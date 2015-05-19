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
        res = None
        if action == "search":
            t.log.info("pre-exec search")
            res = self.search(data)
        elif action == "fetch":
            t.log.info("pre-exec fetch")
            res = self.fetch(data)
        else:
            t.log.error("not action found")
        return res

    def search(self, data):
        t.log.info("searching")
        persons = Person.select().where(
                    Person.name.contains(data)|
                    Person.social_number.contains(data)
                )
        ui = ""
        for person in persons:
            ui_ ="id:%s %s %s" %(person.id, person.name, 
                        person.social_number)
            ui += ui_  + "\n"
            t.log.info(ui_)
        return ui

    def fetch(self, id):
        person = Person.get(Person.id==int(id))
        t.log.info(t.red("person"))
        ui = " %s NS: %s Nombre %s" % (person.id, 
                person.social_number, person.name)
        return ui

