from buyer import *
from mailbox import *
from PIL import Image, ImageTk
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
    # must keep a global reference to these two
    
    # BUYER TAB
    buyerTab = ttk.Frame(tab_control)
    tab_control.add(buyerTab, text='Buy items')
    mailTab = ttk.Frame(tab_control)
    tab_control.add(mailTab, text='Clear mail box')
    
    archerImage = ImageTk.PhotoImage(Image.open('images/archer.png').resize((200, 200), Image.ANTIALIAS))
    archerLabel = tk.Label(buyerTab,
                        justify='center', 
                        font=("-size", 10, "-weight", "bold"),
                        image=archerImage)
    archerLabel.grid(row=5, column=0, pady=40, columnspan=1)
    archerLabel.place(relx=0.5, rely=0.85, anchor='center')
    archerLabel.image=archerImage
    
    buyerLabel = tk.Label(buyerTab, text= 'OPEN THE AUCTION AT THE GAME',
                        justify='center', 
                        font=("-size", 10, "-weight", "bold"))
    buyerLabel.grid(row=0, column=0, pady=10, columnspan=1)
    buyerLabel.place(relx=0.5, rely=0.07, anchor='center')
    
    # BUYER INPUTS
    entryPrice = ttk.Entry(buyerTab)
    entryPrice.insert(0, "Price")
    entryPrice.grid(row=1, column=0, padx=80, pady=(40, 10), sticky="new")
    
    amount = ttk.Entry(buyerTab)
    amount.insert(1, "Amount")
    amount.grid(row=3, column=0, padx=80, pady=(2, 10), sticky="new")
    
    entryName = ttk.Entry(buyerTab)
    entryName.insert(0, "Item")
    entryName.grid(row=4, column=0, padx=80, pady=(2, 10), sticky="new")
    
    boton = ttk.Button(buyerTab, text="Run", style='Accent.TButton',
                       command=lambda:testButton(entryPrice.get(),amount.get(), entryName.get()))
    boton.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
    boton.place(relx=0.5, rely=0.5, anchor='center')
    
    rememberLabel = tk.Label(buyerTab, text= 'IMPORTANT: Remember, press \'Ctrl\' until bot stop \n when is running',
                        anchor='center', 
                        font=("-size", 8, "-weight", "bold"))
    rememberLabel.grid(row=5, column=0, pady=10, columnspan=2)
    rememberLabel.place(relx=0.5, rely=0.85, anchor='center')
    
    # MAILBOX    
    mailLabel = tk.Label(mailTab, text= 'OPEN THE MAILBOX AT THE GAME', 
                         anchor='center', 
                         font=("-size", 10, "-weight", "bold",))
    mailLabel.grid(row=0, column=0, pady=10, columnspan=1)
    mailLabel.place(relx=0.5, rely=0.07, anchor='center')
    
    clearBoton = ttk.Button(mailTab, text="Clear", style='Accent.TButton', command=clearMail)
    clearBoton.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
    clearBoton.place(relx=0.5, rely=0.5, anchor='center')
    
    archerLabel = tk.Label(mailTab,
                        justify='center', 
                        font=("-size", 10, "-weight", "bold"),
                        image=archerImage)
    archerLabel.grid(row=2, column=0, pady=10, columnspan=1)
    archerLabel.place(relx=0.5, rely=0.85, anchor='center')
    archerLabel.image=archerImage
    rememberLabel = tk.Label(mailTab, text= 'IMPORTANT: Remember, press \'Ctrl\' until bot stop \n when is running',
                        justify='center', 
                        font=("-size", 8, "-weight", "bold"))
    rememberLabel.grid(row=2, column=0, pady=245, columnspan=2)
    rememberLabel.place(relx=0.5, rely=0.85, anchor='center')

    tab_control.pack(fill = "both", expand = "yes")