'''
Created on 3 Sep 2012

@author: cgueret
'''
import gtk
from GUI import MainWindow
from Model import Messages

if __name__ == '__main__':
	model = Messages()
	main = MainWindow(model)
	gtk.main()