#!/usr/bin/env python

# example base.py

import pygtk
pygtk.require('2.0')
import gtk

class Base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("GTK hello world!")
        self.window.set_size_request(200,50)
        self.window.set_border_width(10)
        hbox_b = gtk.HBox(False, 0)
        self.window.add(hbox_b)
        label_b = gtk.Label("Hello janague!!!")
        label_b.show()
        hbox_b.pack_start(label_b, False, False, 0)
        hbox_b.show()
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
