from tkinter import *
import black
import matplotlib
from matplotlib import image
import requests
from alpha_vantage.timeseries import TimeSeries
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

from pyparsing import col
from torch import maximum
#Enter your own api from https://www.alphavantage.co/
apiKey= "" 

root = Tk()
root.title("Stockvaluator")
root.geometry("700x400")




def Ticker_Search_button():
    global ticker
    ticker=tickerEntry.get()

    if len(ticker) == 0:
      print("Invalid Ticker")
      tickerStatusFail.grid()
    else:
      print("VALID TICKER")
      print(ticker)
      tickerStatusSuccess.grid()
      stockChartView.grid()
      currentPrice = Stock_Price_Current()
      
      stockPriceCurrent.config(text=currentPrice)
   

    

def Stock_Chart_View_button():
      ts = TimeSeries(key=apiKey, output_format='pandas')
      data, meta_data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='full')
      data['4. close'].plot()
      plt.title="sss"
      plt.show()

def Stock_Price_Current():
  ts = TimeSeries(key=apiKey, output_format='pandas')
  data, meta_data = ts.get_weekly(symbol=ticker)
  close_data = data["4. close"]
  lastPrice = close_data[0]
  stockPriceCurrent.grid()
  stockPriceCurrentStatic1.grid()
  print(lastPrice)
  return(lastPrice)




     

#alpha vnamtage api key, remember to use yourt own api key






#Create objects
tickerEntryButton = Button(root, text="Search", command=Ticker_Search_button)
tickerEntry = Entry(root, width=40, borderwidth=5)

tickerStatusFail= Label(root, width=16, height=1, bg="red", text="Ticker Not Found")
tickerStatusSuccess= Label(root, width=16, height=1, bg="green", text="Ticker Found")

stockChartView= Button(root, text="Open chart", command=Stock_Chart_View_button)
stockPriceCurrentStatic1= Label(root, width=10, height=2, bg="#e0e2ff", text="Last price: ")
stockPriceCurrent= Label(root, width=5, height=2, bg="#e0e2ff", text="")




#middleDivider= Canvas(root, width=1, height= bg="black")

#stockChart= Canvas(root, width=70, height=40)

#Labels txt for 


  
#Design
tickerEntry.grid(row=0, column=0, columnspan=10, padx=(23,10))
tickerEntryButton.grid(row=0, column=11)
tickerStatusFail.grid(row=1, column=0, columnspan=2, padx=(23,0))
tickerStatusFail.grid_remove()
tickerStatusSuccess.grid(row=1, column=0 ,columnspan=2, padx=(23,0))
tickerStatusSuccess.grid_remove()
stockChartView.grid(row=1, column=11)
stockChartView.grid_remove()
stockPriceCurrentStatic1.grid(row=0, column=15, padx=(10,0))
stockPriceCurrentStatic1.grid_remove()
stockPriceCurrent.grid(row=0, column=16, padx=(0,0))
stockPriceCurrent.grid_remove()






#End
root.mainloop()

