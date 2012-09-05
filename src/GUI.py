'''
Created on 3 Sep 2012

@author: cgueret
'''
import gtk
import gobject
from sugar.graphics import style

class Contacts(object):
	def __init__(self):
		model = gtk.ListStore(gobject.TYPE_STRING)
		view = gtk.IconView(model)
		view.set_text_column(0)
		scrollable = gtk.ScrolledWindow()
		scrollable.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
		scrollable.add(view)
		self._widget = scrollable
		
		model.append(['Everyone'])
		model.append(['Toto'])
		
	def get_widget(self):
		self._widget.show_all()
		return self._widget
		

class Messages(object):
	def __init__(self):
		model = gtk.ListStore(gobject.TYPE_STRING)
		view = gtk.IconView(model)
		view.set_text_column(0)
		scrollable = gtk.ScrolledWindow()
		scrollable.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
		scrollable.add(view)
		self._widget = scrollable
		
		model.append(['Bonjour!'])
		
	def get_widget(self):
		self._widget.show_all()
		return self._widget

class Post(object):
	def __init__(self):
		box = gtk.HBox()		
		textview = gtk.TextView()
		send = gtk.Button()
		box.pack_start(textview, expand=True, fill=True)
		box.pack_end(send, expand=False, fill=True)

		self._widget = box
		self._widget.show_all()
		
	def get_widget(self):
		return self._widget
		
class MainWindow(object):
	def __init__(self):
		'''
		Constructor
		'''
		self._contacts = Contacts()
		self._messages = Messages()
		self._post = Post()
		
		# Create the Window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy", self.destroy_cb)
		self.window.connect("key-press-event", self.keypress_cb)
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
