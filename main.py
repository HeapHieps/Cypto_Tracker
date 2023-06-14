import requests 
import tkinter as tk
from datetime import datetime

#-------------Format----------------------------

canva = tk.Tk()
canva.geometry ("400x500")
canva.title ("Crypto Tracker")

canva.minsize(400,500)
canva.configure(bg="LightSteelBlue4")

f1 = ("arial", 22, "bold")
f2 = ("arial", 20, "bold")
f3 = ("arial", 16, "normal")

#-------------Functions------------------------

def GetCrypto(crypto):
    url = f"https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    return response.get("USD")

def Tracker():
    BTC_Prices = GetCrypto("BTC")
    ETH_Prices = GetCrypto("ETH")
    Updatedtime = datetime.now().strftime("%H:%M:%S")

    labelBTCPrice.config(text=f"${BTC_Prices}")
    labelETHPrice.config(text=f"${ETH_Prices}")
    labelTime.config(text = "Updated at: " + Updatedtime)

    canva.after(2000, Tracker) #Update Prices every 2 seconds

#-------------Display-------------------------

labelBTC = tk.Label(canva, text="BitCoin Price", font=f1, bg="LightSteelBlue4")
labelBTC.pack(anchor='nw', padx=2, pady=10) 

labelBTCPrice = tk.Label(canva, font=f2, bg="LightSteelBlue4")
labelBTCPrice.pack(anchor='nw', padx=7) 

labelETH = tk.Label(canva, text="Ethereum Price", font=f1, bg="LightSteelBlue4")
labelETH.pack(anchor='nw', padx=2, pady=10) 

labelETHPrice = tk.Label(canva, font=f2, bg="LightSteelBlue4")
labelETHPrice.pack(anchor='nw', padx=7) 



labelTime = tk.Label(canva, font=f3, bg="LightSteelBlue4")
labelETHPrice.pack(anchor='nw', padx=7) 


Tracker()

canva.mainloop()

