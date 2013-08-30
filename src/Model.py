import random
from time import gmtime, strftime
from calendar import timegm
from sugar import profile
from rdflib import Literal, Namespace
from ers import ERSLocal

OLPC_RESOURCE = Namespace("http://semanticxo.appspot.com/resource/")

class Messages(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.registry = ERSLocal()

    def _new_id(self, part_id):
        return "urn:ers:act:messages:{}:{:04x}".format(part_id, random.randrange(16**4))
    
    def post(self, message):
        '''
        Post a new public message
        '''
        utc_time = gmtime()
        entity = self._new_id(timegm(utc_time))
        timestamp = strftime("%Y-%m-%dT%H:%M:%SZ", utc_time)
        self.registry.add_data(entity, "dcterms:created", timestamp, "g1")
        self.registry.add_data(entity, "sioc:has_creator", Literal(profile.get_nick_name()), "g1")
        self.registry.add_data(entity, "sioc:content", Literal(message), "g1")
        self.registry.add_data(entity, "sioc:addressed_to", OLPC_RESOURCE['public'], "g1")
        self.registry.add_data(entity, "rdf:type", "sioc:MailMessage", "g1")
    
    def get_messages(self):
        '''
        Get the list of messages currently stored locally
        '''
        messages = []
        for (entity, graph) in self.registry.search("rdf:type", "sioc:MailMessage"):
            try:
                data = self.registry.get_annotation(entity)
                message = ', '.join(data["sioc:content"])
                author = ', '.join(data["sioc:has_creator"])
                timestamp = data["dcterms:created"][-1]
                messages.append((timestamp, "{0} (from: {1})".format(message, author)))
            except Exception as e:
                messages.append((0, "error: {0}".format(e)))
        return [m for d, m in sorted(messages)]
