import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

# Tkinter methods
def main_app():
    window.title("LostArk Bot")
    window.geometry('350x400')
    createWindows()
    window.resizable(False, False) 
    window.mainloop()

def createWindows():
    tab_control = ttk.Notebook(window)
    tab = ttk.Frame(tab_control)
    
    tab_control.add(tab, text='Buy items')
    buyerLabel = tk.Label(tab_control, text= 'Open the auction at the game')
    buyerLabel.grid(row=0, column=0, padx=0, pady=(10, 0), sticky="nsew")
    boton = ttk.Button(tab_control, text="Run", style='Accent.TButton')
    boton.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")
    boton.place(x=175, y=150)
    entry = ttk.Entry(buyerLabel)
    entry.insert(0, "Entry")
    entry.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="new")
    
    mailTab = ttk.Frame(tab_control)
    tab_control.add(mailTab, text='Clear mail box')
    lbl1 = tk.Label(mailTab, text= 'Open the mail box at the game', anchor='center')
    lbl1.grid(column=0, row=0)   
    tab_control.pack(expand=1, fill='both')