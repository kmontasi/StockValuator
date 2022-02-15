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

apiKey= "38QZDWCZNZMDR75W"
ticker= "ko"

ts = TimeSeries(key=apiKey, output_format='pandas')
data, meta_data = ts.get_weekly(symbol=ticker)
close_data = data["4. close"]
global lastPrice
lastPrice = close_data[0]


fd=FundamentalData(key=apiKey, output_format='pandas')
  
data, meta_data = fd.get_company_overview(symbol=ticker)

dataOutsandongShares = data["SharesOutstanding"]
dataOutsandongShares = dataOutsandongShares[0]



data, meta_data = fd.get_income_statement_quarterly(symbol=ticker)
dataIncome = data["netIncome"]
dataIncome = float(dataIncome[0])+float(dataIncome[1])+float(dataIncome[2])+float(dataIncome[3])
dataOutsandongShares = data["SharesOutstanding"]
dataOutsandongShares = dataOutsandongShares[0]


def Company_Overview():
  
  data, meta_data = fd.get_company_overview(symbol=ticker)


#financial pricing calculations
#Stocks calculated eps, calculated by COMPANYS PROFITS / OUTSTANDING SHARES
def Stock_Calculated_EPS():
    global eps
    eps = float(dataIncome)/float(dataOutsandongShares)


def Stock_Calculated_PE_Ratio():
  #P/E ratio
  
  print("pe ratio: "+float(lastPrice)/eps) 

def Grahams_Price():
  data, meta_data = fd.get_company_overview(symbol=ticker)
  bookValue = data["BookValue"]
  grahamsPricingModel=22.5*eps* float(bookValue)