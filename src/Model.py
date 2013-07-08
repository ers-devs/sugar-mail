'''
Created on 15 Sep 2012

@author: cgueret
'''
import uuid
import ers
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
    
    def post(self, message):
        '''
        Post a new public message
        '''
        uid = str(uuid.uuid4())
        self.registry.add_data(uid, "message", Literal(message), "g1")
        self.registry.add_data(uid, "author", Literal(profile.get_nick_name()), "g1")
        self.registry.add_data(uid, "share", OLPC_RESOURCE['public'], "g1")
        self.registry.add_data(uid, "category", "Message", "g1")
    
    def get_messages(self):
        '''
        Get the list of messages currently stored locally
        '''
        messages = []

        for (entity, graph) in self.registry.search("category", "Message"):
            data = self.registry.get_data(entity, graph)
            message = ', '.join(data['message'])
            author = ', '.join(data['author'])
            messages.append("%s (from: %s)" % (message, author))
        return messages
