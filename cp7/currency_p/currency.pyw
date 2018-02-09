#!/usr/bin/env python3

import os
op = os.path

import sys
sys.path.append(op.abspath(op.join(os.path.dirname(__file__),
    "../..")))
import tkinter as tk
import Main
import TkUtil

def main():
    app = tk.Tk()
    app.title("Currency")
    TkUtil.set_application_icons(app, os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 
        "images"))
    Main.Window(app)
    app.mainloop()

if __name__ == '__main__':
    main()