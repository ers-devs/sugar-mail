'''
Created on 15 Sep 2012

@author: cgueret
'''
from semanticxo import graphstore, util
from rdflib.term import Literal

class Messages(object):
	def __init__(self):
		pass
	
	def post(self, message):
		print "post " + message
		graph = graphstore.get_instance().create_object()
		entry = graph.create_entry(uid=None, category='Message')
		entry.add("message", Literal(message))
		graph.add_share(util.public_uri())
		graphstore.get_instance().persist_object(graph)
	
	def get_messages(self):
		pass