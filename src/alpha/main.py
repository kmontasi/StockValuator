from cmath import sqrt
from tkinter import *
from turtle import st
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

#ColorPalette
Base1 = "#212f45"
SearchFail = "#780000"
SearchSuccess = "#0b525b"
MainWidgets = "#355070"

#Enter your own api from https://www.alphavantage.co/
apiKey= "RU6TFT32YF8UFRMZ" 
#
#38QZDWCZNZMDR75W

root = Tk()
root.title("Stockvaluator")
root.geometry("700x400")
root.configure(background=Base1)


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
    
    

    currentPrice = Stock_Price_Current() 
    stockPriceCurrent.config(text=currentPrice)




    Company_Overview()
    get_income_statement_quarterly()
    E_P_S()
    P_E()
    Grahams_Number()
    #print(eps)
    #print(pe)
    #print(grahamsPricingModel)

    StockEPSCurrent.grid() 
    StockEPSCurrentStatic1.grid()
    StockEPSCurrent.config(text=eps)
    RealStockEPSCurrent.grid() 
    RealStockEPSCurrentStatic1.grid()

    StockPECurrent.grid() 
    StockPECurrentStatic1.grid()
    StockPECurrent.config(text=pe)
    RealStockPECurrent.grid() 
    RealStockPECurrentStatic1.grid()

    GrahamsNumber.grid()
    GrahamsNumberStatic1.grid()
    GrahamsNumber.config(text=grahamsNumber)
    RealGrahamsNumber.grid()
    RealGrahamsNumberStatic1.grid()
    
  

   

    

def Stock_Chart_View_button(): 
  data, meta_data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='full')
  data['4. close'].plot()
  plt.title="sss"
  plt.show()

def Stock_Price_Current():
  data, meta_data = ts.get_weekly(symbol=ticker)
  close_data = data["4. close"]
  global lastPrice
  lastPrice = close_data[0]
  stockPriceCurrent.grid()
  stockPriceCurrentStatic1.grid()
  print(lastPrice)
  return(lastPrice)

def Company_Overview():
    
    data, meta_data = fd.get_company_overview(symbol=ticker)

    global dataOutsandongShares
    dataOutsandongShares = data["SharesOutstanding"]
    dataOutsandongShares = dataOutsandongShares[0]

    global bookValue
    bookValue = data["BookValue"]
    
def get_income_statement_quarterly():

    data, meta_data = fd.get_income_statement_quarterly(symbol=ticker)
    global dataIncome
    dataIncome = data["netIncome"]
    dataIncome = float(dataIncome[0])+float(dataIncome[1])+float(dataIncome[2])+float(dataIncome[3])
    print(float(dataIncome)/float(dataOutsandongShares))



    

def E_P_S():
    global eps
    raweps = float(dataIncome)/float(dataOutsandongShares)
    eps = str(raweps)
    eps = eps[0:5]
    

    

def P_E():
  global pe
  rawpe = lastPrice/float(eps)
  pe = str(rawpe)
  pe = pe[0:5]
  
  

def Grahams_Number():
  global grahamsNumber
  rawgrahamsNumber =(22.5*float(eps)) * float(bookValue)
  rawgrahamsNumber = sqrt(rawgrahamsNumber)
  grahamsNumber =str(rawgrahamsNumber)
  grahamsNumber =grahamsNumber[1:6]
    








#Create objects
tickerEntryButton = Button(root, text="Search", command=Ticker_Search_button)
tickerEntry = Entry(root, width=40, borderwidth=5)

tickerStatusFail = Label(root, width=16, height=1, bg=SearchFail, text="Ticker Not Found")
tickerStatusSuccess = Label(root, width=16, height=1, bg=SearchSuccess, text="Ticker Found")

stockChartView = Button(root, text="Open chart", command=Stock_Chart_View_button)

stockPriceCurrentStatic1 = Label(root, width=20, height=2, bg=MainWidgets, text="Last price: ")
stockPriceCurrent = Label(root, width=5, height=2, bg=MainWidgets, text="")
RealstockPriceCurrentStatic1 = Label(root, width=20, height=2, bg=MainWidgets, text="Last price: ")
RealstockPriceCurrent = Label(root, width=5, height=2, bg=MainWidgets, text="")

StockEPSCurrentStatic1 = Label(root, width=20, height=2, bg=MainWidgets, text="TTP EPS value: ")
StockEPSCurrent = Label(root, width=5, height=2, bg=MainWidgets, text="")
RealStockEPSCurrentStatic1 = Label(root, width=20, height=2, bg=MainWidgets, text="TTP EPS value: ")
RealStockEPSCurrent = Label(root, width=5, height=2, bg=MainWidgets, text="")

StockPECurrentStatic1 = Label(root, width=20, height=2, bg=MainWidgets, text=" 'good' P/E value: ")
StockPECurrent = Label(root, width=5, height=2, bg=MainWidgets, text="")
RealStockPECurrentStatic1 = Label(root, width=20, height=2, bg=MainWidgets, text=" P/E value: ")
RealStockPECurrent = Label(root, width=5, height=2, bg=MainWidgets, text="")

GrahamsNumberStatic1 = Label(root, width=20, height=2, bg=MainWidgets, text="Grahams Number: ")
GrahamsNumber = Label(root, width=5, height=2, bg=MainWidgets, text="")
RealGrahamsNumberStatic1 = Label(root, width=20, height=2, bg=MainWidgets, text="Grahams Number: ")
RealGrahamsNumber = Label(root, width=5, height=2, bg=MainWidgets, text="")

###Checkbutton(root, text="EPS", variable=var1).grid(row=0, sticky=W)


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

stockPriceCurrentStatic1.grid(row=0, column=15, columnspan=2, padx=(10,0))
stockPriceCurrentStatic1.grid_remove()
stockPriceCurrent.grid(row=0, column=17, padx=(0,0))
stockPriceCurrent.grid_remove()

RealstockPriceCurrentStatic1.grid(row=0, column=18, columnspan=2, padx=(10,0))
RealstockPriceCurrentStatic1.grid_remove()
RealstockPriceCurrent.grid(row=0, column=20, padx=(0,0))
RealstockPriceCurrent.grid_remove()

StockEPSCurrentStatic1.grid(row=1, column=15, columnspan=2, padx=(10,0))
StockEPSCurrentStatic1.grid_remove()
StockEPSCurrent.grid(row=1, column=17, padx=(0,0))
StockEPSCurrent.grid_remove()

RealStockEPSCurrentStatic1.grid(row=1, column=18, columnspan=2, padx=(10,0))
RealStockEPSCurrentStatic1.grid_remove()
RealStockEPSCurrent.grid(row=1, column=20, padx=(0,0))
RealStockEPSCurrent.grid_remove()

StockPECurrentStatic1.grid(row=2, column=15, columnspan=2, padx=(10,0))
StockPECurrentStatic1.grid_remove()
StockPECurrent.grid(row=2, column=17, padx=(0,0))
StockPECurrent.grid_remove()

RealStockPECurrentStatic1.grid(row=2, column=18, columnspan=2, padx=(10,0))
RealStockPECurrentStatic1.grid_remove()
RealStockPECurrent.grid(row=2, column=20, padx=(0,0))
RealStockPECurrent.grid_remove()

GrahamsNumberStatic1.grid(row=3, column=15, columnspan=2, padx=(10,0))
GrahamsNumberStatic1.grid_remove()
GrahamsNumber.grid(row=3, column=17, padx=(0,0))
GrahamsNumber.grid_remove()

RealGrahamsNumberStatic1.grid(row=3, column=18, columnspan=2, padx=(10,0))
RealGrahamsNumberStatic1.grid_remove()
RealGrahamsNumber.grid(row=3, column=20, padx=(0,0))
RealGrahamsNumber.grid_remove()



#End
root.mainloop()

