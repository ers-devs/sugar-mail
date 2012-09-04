'''
Created on 3 Sep 2012

@author: cgueret
'''
import gtk
from sugar.graphics import style

class Dialogs(object):
	def __init__(self):
		self._widget = 
class MainWindow(object):
	def __init__(self):
		'''
		Constructor
		'''
		self._dialogs = Dialogs()
		
		# Create the Window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy", self.destroy_cb)
		self.window.connect("key-press-event", self.keypress_cb)
		self.window.set_border_width(style.DEFAULT_PADDING)
		self.window.set_size_request(600, 450)
		self.window.set_position(gtk.WIN_POS_CENTER)
		
		scrollable = gtk.ScrolledWindow()
		scrollable.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
		scrollable.add(self.mess)

		left_right = gtk.VBox()
		left_right.pack_start(dialogs, expand=True, fill=True)
		left_right.pack_end(button, expand=False, fill=True)

		# Pack everything
		self.window.show_all()
	
	def keypress_cb(self, widget, event):
		if event.keyval == gtk.keysyms.Escape or event.keyval == gtk.keysyms.Return :
			gtk.main_quit()
	
	def destroy_cb(self, widget, event=None):
		gtk.main_quit()
