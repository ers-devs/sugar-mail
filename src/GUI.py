'''
Created on 3 Sep 2012

@author: cgueret
'''
import gtk
import gobject

class Contacts(object):
    def __init__(self, parent):
        self._parent = parent
        
        model = gtk.TreeStore(gobject.TYPE_STRING)
        view = gtk.TreeView(model)
        viewcolumn = gtk.TreeViewColumn('Visibility')
        view.append_column(viewcolumn)
        cell = gtk.CellRendererText()
        viewcolumn.pack_start(cell, True)
        viewcolumn.add_attribute(cell, 'text', 0)
        scrollable = gtk.ScrolledWindow()
        scrollable.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        scrollable.add(view)
        scrollable.set_border_width(2)
        self._widget = scrollable
        
        model.append(None, ['Public'])
        
    def get_widget(self):
        self._widget.show_all()
        return self._widget
        

class Messages(object):
    def __init__(self, parent):
        self._parent = parent
        
        self._model = gtk.TreeStore(gobject.TYPE_STRING)
        view = gtk.TreeView(self._model)
        viewcolumn = gtk.TreeViewColumn('Messages')
        view.append_column(viewcolumn)
        cell = gtk.CellRendererText()
        viewcolumn.pack_start(cell, True)
        viewcolumn.add_attribute(cell, 'text', 0)
        scrollable = gtk.ScrolledWindow()
        scrollable.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        scrollable.add(view)
        scrollable.set_border_width(2)
        self._widget = scrollable
        
        
    def get_widget(self):
        self._widget.show_all()
        return self._widget

    def set_list(self, messages):
        '''
        Set a new content for the list of messages
        '''
        self._model.clear()
        for message in messages:
            self._model.append(None, [message])
        
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
        self._messages = Messages(self)
        self._post = Post(self)
        
        self._widget = gtk.VBox()
        self._widget.pack_start(self._messages.get_widget(), expand=True, fill=True)
        self._widget.pack_end(self._post.get_widget(), expand=False, fill=True)

        # Refresh the display
        self.refresh_messages()
        
        # Add a timer to refresh the display from time to time
        self._timer = gobject.timeout_add(5000, self.refresh_messages)
    
    def get_widget(self):
        self._widget.show_all()
        return self._widget
            
    def post_message(self, message):
        '''
        Function called by the UI component to post a message
        '''
        # Post the message
        self._model.post(message)
        # Refresh the display
        self.refresh_messages()
        
    def refresh_messages(self):
        '''
        Function called to refresh the messages list
        '''
        # Get the messages
        messages = self._model.get_messages()
        # Update the list
        self._messages.set_list(messages)
        # Return True so that the timer continues to refresh
        return True