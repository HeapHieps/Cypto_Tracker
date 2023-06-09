import requests 
import tkinter as tk
from datetime import datetime

def Tracker():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    Updatedtime = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text = str(price)+ " $")
    labelTime.config(text = "Updated at: " + Updatedtime)

    canvas.after(5000, Tracker) #Update Prices every 5 seconds

canvas = tk.Tk()
canvas.geometry ("400x500")
canvas.title ("Tracker")

f1 = ("arial", 22, "bold")
f2 = ("arial", 20, "bold")
f3 = ("arial", 16, "normal")

label = tk.Label(canvas, text="BitCoin Price", font=f1)
label.pack(anchor='w', padx=10, pady=10) 

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(anchor='w', padx=10) 

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(anchor='center', pady=50)

Tracker()

canvas.mainloop()

