'''
Created on 3 Sep 2012

@author: cgueret
'''
import gtk
import gobject
from sugar.graphics import style

class Contacts(object):
	def __init__(self, parent):
		self._parent = parent
		
		model = gtk.TreeStore(gobject.TYPE_STRING)
		view = gtk.TreeView(model)
		viewcolumn = gtk.TreeViewColumn('Contacts')
		view.append_column(viewcolumn)
		cell = gtk.CellRendererText()
		viewcolumn.pack_start(cell, True)
		viewcolumn.add_attribute(cell, 'text', 0)
		scrollable = gtk.ScrolledWindow()
		scrollable.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
		scrollable.add(view)
		scrollable.set_border_width(2)
		self._widget = scrollable
		
		model.append(None, ['Everyone'])
		model.append(None, ['Toto'])
		
	def get_widget(self):
		self._widget.show_all()
		return self._widget
		

class Messages(object):
	def __init__(self, parent):
		self._parent = parent
		
		model = gtk.ListStore(gobject.TYPE_STRING)
		view = gtk.IconView(model)
		view.set_text_column(0)
		scrollable = gtk.ScrolledWindow()
		scrollable.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
		scrollable.add(view)
		scrollable.set_border_width(2)
		self._widget = scrollable
		
		model.append(['Bonjour!'])
		
	def get_widget(self):
		self._widget.show_all()
		return self._widget

class Post(object):
	'''
	Interface for posting a new message
	'''
	def __init__(self, parent):
		self._parent = parent
		self._text = gtk.TextBuffer()
		
		box = gtk.HBox()		
		box.set_border_width(2)
		textview = gtk.TextView(self._text)
		send = gtk.Button(label='Send message')
		box.pack_start(textview, expand=True, fill=True)
		box.pack_end(send, expand=False, fill=True)
		
		# Connect the call backs
		send.connect("clicked", self.send_message_cb)
		
		self._widget = box
		self._widget.show_all()
		
	def get_widget(self):
		'''
		Return the widget for this UI component
		'''
		return self._widget
	
	def send_message_cb(self, widget, event=None):
		'''
		Call back for when the submit button is pressed
		'''
		text = self._text.get_text(start = self._text.get_start_iter(), end = self._text.get_end_iter())
		self._parent.post_message(text)
		
class MainWindow(object):
	def __init__(self, model):
		'''
		Constructor
		'''
		self._model = model
		self._contacts = Contacts(self)
		self._messages = Messages(self)
		self._post = Post(self)
		
		# Create the Window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy", self.destroy_cb)
		#self.window.connect("key-press-event", self.keypress_cb)
		self.window.set_border_width(style.DEFAULT_PADDING)
		self.window.set_size_request(600, 450)
		self.window.set_position(gtk.WIN_POS_CENTER)

		main_box = gtk.HBox()
		main_box.pack_start(self._contacts.get_widget(), expand=False, fill=True)
		right_box = gtk.VBox()
		right_box.pack_start(self._messages.get_widget(), expand=True, fill=True)
		right_box.pack_end(self._post.get_widget(), expand=False, fill=True)
		main_box.pack_end(right_box, expand=True, fill=True)

		# Pack everything
		self.window.add(main_box)
		self.window.show_all()
	
	def keypress_cb(self, widget, event):
		if event.keyval == gtk.keysyms.Escape or event.keyval == gtk.keysyms.Return :
			gtk.main_quit()
	
	def destroy_cb(self, widget, event=None):
		gtk.main_quit()
		
	def post_message(self, message):
		'''
		Function called by the UI component to post a message
		'''
		# Post the message
		self._model.post(message)
		# Refresh the display
	
