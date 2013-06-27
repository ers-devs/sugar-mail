'''
Created on 15 Sep 2012

@author: cgueret
'''

from rdflib.term import Literal
from sugar import profile

class Messages(object):
	
	def __init__(self):
		'''
		Constructor
		'''
		pass

	
	def post(self, message):
		'''
		Post a new public message
		'''
		# # Get a grasp over the graph store
		# gstore = graphstore.get_instance()
		
		# # Create a new graph
		# graph = gstore.create_graph()
		
		# # Create a resource of type Message and populate it
		# resource = graph.create_resource(uid=None, category='Message')
		# resource.add("message", Literal(message))
		# resource.add("author", Literal(profile.get_nick_name()))
		
		# # Allow this graph to be shared with other XOs
		# graph.add_share(util.public_uri())
		
		# # Persist the graph
		# gstore.persist_graph(graph)

	
	def get_messages(self):
		'''
		Get the list of messages currently stored locally
		'''
		# Array for the results
		messages = []
		
		# # Get a grasp over the graph store
		# gstore = graphstore.get_instance()
		
		# # Get the list of graphs that contain messages
		# graph_ids = gstore.get_graphs_list(restrict='Message')
		
		# for graph_id in graph_ids[::-1]:
			
		# 	# Load the graph
		# 	graph = gstore.get_graph(graph_id)
			
		# 	# Get the list of resources that are of type "Message"
		# 	# (a single graph could be used to store several messages)
		# 	resource_ids = graph.get_resources_list(restrict='Message')
			
		# 	for resource_id in resource_ids:
				
		# 		# Load the resource
		# 		resource = graph.get_resource(resource_id)
				
		# 		# Get the properties we are interested in
		# 		message = resource.get("message")[0]
		# 		author = resource.get("author")[0]
				
		# 		# Push that to the result list
		# 		messages.append("%s (from: %s)" % (message, author))
				
		# Return the messages
		return messages
	