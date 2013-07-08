'''
Created on 3 Sep 2012

@author: cgueret
'''
import gtk
from GUI import MainWindow
from Model import Messages
from sugar.graphics import style

def destroy_cb(widget):
    '''
    Called when the application is destroyed
    '''
    gtk.main_quit()

if __name__ == '__main__':
    model = Messages()
    main = MainWindow(model)
    
    # Create the Window
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.connect("destroy", destroy_cb)
    window.set_border_width(style.DEFAULT_PADDING)
    window.set_size_request(600, 450)
    window.set_position(gtk.WIN_POS_CENTER)

    # Pack everything
    window.add(main.get_widget())
    window.show_all()

    # Start gtk
    gtk.main()