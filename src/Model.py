'''
Created on 15 Sep 2012

@author: cgueret
'''
import uuid
import time
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
        self.registry.add_data(uid, "time", time.time(), "g1")
    
    def get_messages(self):
        '''
        Get the list of messages currently stored locally
        '''
        messages = []
        for (entity, graph) in self.registry.search("category", "Message"):
            try:
                data = self.registry.get_annotation(entity)
                message = ', '.join(data['message'])
                author = ', '.join(data['author'])
                timestamp = data['time'][-1]
                messages.append((timestamp, "{0} (from: {1})".format(message, author)))
            except Exception as e:
                messages.append((0, "fail {0}".format(e)))
        return [m for d, m in sorted(messages)]
