import os
import sys
import urllib
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
Spinbox = ttk.Spinbox if hasattr(ttk, "Spinbox") else tk.Spinbox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
import Rates
import TkUtil

class Window(ttk.Frame):
    def __init__(self, *args):
        super().__init__()
        self.create_variables()
        self.create_widgets()
        self.create_layout()
        self.create_bindings()
        self.currency_from_combobox.focus()
        self.after(10, self.get_rate)


    def create_variables(self):
        self.currency_from = tk.StringVar() 
        self.currency_to = tk.StringVar()
        

    def get_rate(self):
        try:
            self.rates = Rates.get()
            self.populate_comboboxes()
        except urllib.error.URLError as err :
            messagebox.showerror("Currency \u2014 Error", str(err),parent=self)
            self.quit()


    def populate_comboboxes(self):
        currencies = sorted(self.rates.keys())
        for combobox in (self.currency_from_combobox, self.currency_to_combobox):
            combobox.state(("readonly",))
            combobox.config(value=currencies)
        TkUtil.set_combobox_item(self.currency_from_combobox, "test")
        TkUtil.set_combobox_item(self.currency_to_combobox, "test2")
        self.calculate()


    def create_widgets(self):
        self.currency_from_combobox = ttk.Combobox(self,
            textvariable=self.currency_to)
        self.currency_to_combobox = ttk.Combobox(self,
            textvariable=self.currency_to)
        

    def validate(self, number):
        return TkUtil.validate_spinbox_float(self.amount_spinbox, number)

    
    def create_layout(self):
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.minsize(150, 40)

        self.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W ))
        self.columnconfigure(0,weight=2)
        self.columnconfigure(1,weight=1)

        padWE = dict(sticky=(tk.W, tk.E), padx="0.5m", pady="0.5m")
        self.currency_from_combobox.grid(row=0, column=0, **padWE)
        self.currency_to_combobox.grid(row=1, column=0, **padWE)

    def create_bindings(self):
        self.currency_from_combobox.bind("<<ComboboxSelected>>", self.calculate)
        self.currency_to_combobox.bind("<<ComboboxSelected>>", self.calculate)
        self.master.bind("<Escape>", lambda event: self.quit())

    def calculate(self, event=None):
        pass
        # from_curency = self.currency_from.get()
        # to_curency = self.currency_to.get()

def main():
    pass

if __name__ == '__main__':
    main()
    
        