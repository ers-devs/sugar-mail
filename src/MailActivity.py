'''
Created on 28 Sep 2012

@author: cgueret
'''
from sugar.activity import activity
from GUI import MainWindow
from Model import Messages
import logging

logger = logging.getLogger('mail-activity')

class MailActivity(activity.Activity):
	def __init__(self, handle):
		# Init
		activity.Activity.__init__(self, handle)
		
		# Configure the toolbox
		toolbox = activity.ActivityToolbox(self)
		activity_toolbar = toolbox.get_activity_toolbar()
		activity_toolbar.keep.props.visible = False
		activity_toolbar.share.props.visible = False
		self.set_toolbox(toolbox)
		toolbox.show()
		
		# Create the application
		model = Messages()
		main = MainWindow(model)
		widget = main.get_widget()
		
		# pack
		self.set_canvas(widget)
		widget.grab_focus()
		