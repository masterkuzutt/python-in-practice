#!/usr/bin/env python3
# Copyright © 2012-13 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
    "..")))
import tkinter as tk
import Main
import TkUtil
from Globals import *


def main():
    app = tk.Tk()
    # たぶん画面を非表示にして置く設定。
    app.withdraw()

    app.title(APPNAME)
 
    app.option_add("*tearOff", False)
    
    # icon の設定をしているだけ。
    TkUtil.set_application_icons(app, os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "images"))
    # そしてmainに渡す。全部meinでよくない？
    window = Main.Window(app)

    # ????
    # app.protocol("WM_DELETE_WINDOW", window.close)
    
    # withdrawの反対　ちらつきがどうとか言っていたやつか？
    app.deiconify()

    app.mainloop()


main()
