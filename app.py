from buyer import *
from mailbox import *
from noafk import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



window = tk.Tk()
window.tk.call("source", "azure.tcl")
window.tk.call("set_theme", "dark")

# Tkinter methods
def main_app():
    window.title("LostArk Bot")
    window.geometry('350x450')
    createWindows()
    window.resizable(False, False) 
    window.attributes('-topmost',True)
    window.mainloop() 

def createWindows():
    tab_control = ttk.Notebook(window)
    # must keep a global reference to these two
    archerImage = ImageTk.PhotoImage(Image.open('images/archer.png').resize((200, 200), Image.ANTIALIAS))
    
    buyerTab = ttk.Frame(tab_control)
    tab_control.add(buyerTab, text='Buy items')
    mailTab = ttk.Frame(tab_control)
    tab_control.add(mailTab, text='Clear mail box')
    noAfkTab = ttk.Frame(tab_control)
    tab_control.add(noAfkTab, text='No Afk')
    
    # BUYER
    buyerLabel = tk.Label(buyerTab, text= 'OPEN THE AUCTION AT THE GAME',
                        justify='center', 
                        font=("-size", 10, "-weight", "bold"))
    buyerLabel.grid(row=0, column=0, pady=10, columnspan=1)
    buyerLabel.place(relx=0.5, rely=0.07, anchor='center')
    
    entryPrice = ttk.Entry(buyerTab)
    entryPrice.insert(0, "Price (Integer)")
    entryPrice.grid(row=1, column=0, padx=80, pady=(40, 10), sticky="new")
    
    amount = ttk.Entry(buyerTab)
    amount.insert(1, "Amount (Integer)")
    amount.grid(row=3, column=0, padx=80, pady=(2, 10), sticky="new")

    entryName = ttk.Entry(buyerTab)
    entryName.insert(0, "Item")
    entryName.grid(row=4, column=0, padx=80, pady=(2, 10), sticky="new")
    
    boton = ttk.Button(buyerTab, text="Run", style='Accent.TButton', 
        command=lambda:buy_item(int(entryPrice.get()),int(amount.get()), entryName.get()))
    boton.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
    boton.place(relx=0.5, rely=0.5, anchor='center')
    
    bottomLabel(buyerTab)
    
    # MAILBOX    
    mailLabel = tk.Label(mailTab, text= 'OPEN THE MAILBOX AT THE GAME', 
                         anchor='center', 
                         font=("-size", 10, "-weight", "bold",))
    mailLabel.grid(row=0, column=0, pady=10, columnspan=1)
    mailLabel.place(relx=0.5, rely=0.07, anchor='center')
    
    clearBoton = ttk.Button(mailTab, text="Clear", style='Accent.TButton', command=clearMail)
    clearBoton.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
    clearBoton.place(relx=0.5, rely=0.5, anchor='center')
    
    bottomLabel(mailTab)

    # NO AFK
    noAfkLabel = tk.Label(noAfkTab, text= 'BE FAR OF ANY NPC TO AVOID CLIC', 
                         anchor='center', 
                         font=("-size", 10, "-weight", "bold",))
    noAfkLabel.grid(row=1, column=0, pady=10, columnspan=1)
    noAfkLabel.place(relx=0.5, rely=0.07, anchor='center')

    labelTop = tk.Label(noAfkLabel, text = "Choose your mouse clic to move at the game")
    labelTop.place(relx=0.5, rely=0.09, anchor='center')
    selectMove = ttk.Combobox(noAfkLabel, state="readonly")
    selectMove["values"] = ["right", "left"]
    selectMove.grid(row=4, column=0, padx=80, pady=(230, 10), sticky="new")
    
    noAfkButton = ttk.Button(noAfkTab, text="No Afk", style='Accent.TButton', command=run_no_afk)
    noAfkButton.grid(row=5, column=0, padx=5, pady=100, sticky="nsew")
    noAfkButton.place(relx=0.5, rely=0.5, anchor='center')
    
    bottomLabel(noAfkTab)

    tab_control.pack(fill = "both", expand = "yes")


def bottomLabel(tab):
    archerImage = ImageTk.PhotoImage(Image.open('images/archer.png').resize((200, 200), Image.ANTIALIAS))
    archerLabel = tk.Label(tab,
                    justify='center', 
                    font=("-size", 10, "-weight", "bold"),
                    image=archerImage)
    archerLabel.grid(row=2, column=0, pady=10, columnspan=1)
    archerLabel.place(relx=0.5, rely=0.85, anchor='center')
    archerLabel.image=archerImage
    rememberLabel = tk.Label(tab, text= 'IMPORTANT: Remember, keep press \'Ctrl\' until bot \n stop when is running',
                        justify='center', 
                        font=("-size", 8, "-weight", "bold"))
    rememberLabel.grid(row=2, column=0, pady=245, columnspan=2)
    rememberLabel.place(relx=0.5, rely=0.85, anchor='center')
