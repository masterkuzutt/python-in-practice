import os 
import sys
import tkinter as tk 
import tkinter.ttk as ttk 
Spinbox = ttk.Spinbox if hasattr(ttk, "Spinbox") else tk.Spinbox
if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import Board
import TkUtil
import TkUtil.Dialog
from Gobals import * 


class Window(TkUtil.Dialog.Dialog):

    def __init__(self, masterm board):
        self.board = board
        super().__init__(master, "Preference \u2014{}".format(APPNAME),TkUtil.Dialog.OK_BUTTON|TkUtil.Dialog.CANCEL_BUTTON)

