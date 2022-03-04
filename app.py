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
    buyerTab = ttk.Frame(tab_control)
    
    tab_control.add(buyerTab, text='Buy items')
    
    buyerLabel = tk.Label(buyerTab, text= 'OPEN THE AUCTION AT THE GAME',
                        justify='center', 
                        font=("-size", 10, "-weight", "bold"))
    buyerLabel.grid(row=0, column=0, pady=10, columnspan=1)
    
    boton = ttk.Button(buyerTab, text="Run", style='Accent.TButton')
    boton.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
    boton.place(relx=0.5, rely=0.5, anchor='center')
    
    entryPrice = ttk.Entry(buyerTab)
    entryPrice.insert(0, "Price")
    entryPrice.grid(row=1, column=0, padx=80, pady=(30, 10), sticky="new")
    
    entryName = ttk.Entry(buyerTab)
    entryName.insert(0, "Item")
    entryName.grid(row=4, column=0, padx=80, pady=(5, 10), sticky="new")
    
    rememberLabel = tk.Label(buyerTab, text= 'IMPORTANT: Remember, press h until bot stop \n when is running',
                        anchor='center', 
                        font=("-size", 8, "-weight", "bold"))
    rememberLabel.grid(row=5, column=0, pady=50, columnspan=2)
    
    # MAILBOX
    mailTab = ttk.Frame(tab_control)
    tab_control.add(mailTab, text='Clear mail box')
    
    mailLabel = tk.Label(mailTab, text= 'OPEN THE MAILBOX AT THE GAME', 
                         justify='center', 
                         font=("-size", 10, "-weight", "bold"))
    mailLabel.grid(row=0, column=0, pady=10, columnspan=1)
    
    boton = ttk.Button(mailTab, text="Clear", style='Accent.TButton')
    boton.grid(row=3, column=1, padx=5, pady=10, sticky="nsew")
    boton.place(relx=0.5, rely=0.5, anchor='center')
    
    rememberLabel = tk.Label(mailTab, text= 'IMPORTANT: Remember, press h until bot stop \n when is running',
                        justify='center', 
                        font=("-size", 8, "-weight", "bold"))
    rememberLabel.grid(row=5, column=0, pady=50, columnspan=2)
    
    tab_control.pack(expand=1, fill='both')