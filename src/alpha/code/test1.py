from tkinter import *
import black
import matplotlib
from matplotlib import image
import requests
from alpha_vantage.timeseries import *
from alpha_vantage.fundamentaldata import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

from pyparsing import col
from torch import maximum


#Enter your own api from https://www.alphavantage.co/
apiKey= "38QZDWCZNZMDR75W" 

root = Tk()
root.title("Stockvaluator")
root.geometry("700x400")


fd=FundamentalData(key=apiKey, output_format='pandas')    
ts = TimeSeries(key=apiKey, output_format='pandas')
    

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
      Weekly()
      currentPrice = lastPrice() 
      stockPriceCurrent.config(text=currentPrice)
      



def Weekly():
    data, meta_data = ts.get_weekly(symbol=ticker)
    global lastPrice
    close_data = data["4. close"]
    lastPrice = close_data[0]
    stockPriceCurrent.grid()
    stockPriceCurrentStatic1.grid()
    print(lastPrice)
    
    


def Intraday():
    data, meta_data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='full')
    data['4. close'].plot()
    plt.title="sss"
    plt.show()
    #for plotting

    
    


#def Company_Overview():
   ## data, meta_data = ts.get_weekly(symbol=ticker)
   # close_data = data["4. close"]

def Company_Overview():
    
    data, meta_data = fd.get_company_overview(symbol=ticker)

    global dataOutsandongShares
    dataOutsandongShares = data["SharesOutstanding"]
    dataOutsandongShares = dataOutsandongShares[0]

    global bookValue
    bookValue = data["BookValue"]
    
def get_income_statement_quarterly():

    data, meta_data = fd.get_income_statement(symbol=ticker)
    global dataIncome
    dataIncome = data["netIncome"]
    dataIncome = float(dataIncome[0])+float(dataIncome[1])+float(dataIncome[2])+float(dataIncome[3])
    
    
   
    #print("eps: "+eps)
    #print(float(dataIncome)/float(dataOutsandongShares))



    

def EPS():
    global eps
    eps = float(dataIncome)/float(dataOutsandongShares)

def PE():
    global lastPrice
    lastprice = float(lastPrice)

def Grahams_Pricing_Model():
    global grahamsPricingModel
    grahamsPricingModel=22.5*eps* float(bookValue)





#Create objects
tickerEntryButton = Button(root, text="Search", command=Ticker_Search_button)
tickerEntry = Entry(root, width=40, borderwidth=5)

tickerStatusFail= Label(root, width=16, height=1, bg="red", text="Ticker Not Found")
tickerStatusSuccess= Label(root, width=16, height=1, bg="green", text="Ticker Found")

stockChartView= Button(root, text="Open chart", command=Intraday)
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


moi = "helloo"

