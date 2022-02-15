def Stock_Fundamentals():
  fd=FundamentalData(key=apiKey, output_format='pandas')
  data, meta_data = fd.get_company_overview(symbol=ticker)
  dataOutsandongShares = data["SharesOutstanding"]
  dataOutsandongShares = dataOutsandongShares[0]


#financial pricing calculations
#Stocks calculated eps, calculated by COMPANYS PROFITS / OUTSTANDING SHARES
def Stock_Calculated_EPS():
  data, meta_data = fd.get_income_statement_quarterly(symbol=ticker)
  dataIncome = data["netIncome"]
  #print(data)
  dataIncome = float(dataIncome[0])+float(dataIncome[1])+float(dataIncome[2])+float(dataIncome[3])
  #print(dataIncome)
  eps = float(dataIncome)/float(dataOutsandongShares)
  #print("eps: "+eps)
  #print(float(dataIncome)/float(dataOutsandongShares))  

def Stock_Calculated_PE_Ratio():
  #P/E ratio
  #print("pe ratio: "+float(lastPrice)/eps) 

def Grahams_Price():
  data, meta_data = fd.get_company_overview(symbol=ticker)
  bookValue = data["BookValue"]

grahamsPricingModel=22.5*eps* float(bookValue)