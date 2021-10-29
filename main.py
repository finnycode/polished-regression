import datetime
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

name_list = []
ticker_any = input('ticker: ')
print("Warning: the more days you predict into the future, the less accurate the model is")
print("")
day_num = int(input("Amount of days you want to predict into the future(0 means 1): "))

ticker_any = ticker_any.upper()
og_link = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
stock_link = "https://finance.yahoo.com/quote/" + ticker_any + "?p=" + ticker_any + "&.tsrc=fin-srch"
csv_link = "https://query1.finance.yahoo.com/v7/finance/download/" + ticker_any + "?period1=-252374400&period2=11635348709&interval=1d&events=history&includeAdjustedClose=true"
import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers"
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(csv_link,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() 
csv_file = open('values.csv', 'wb')
csv_file.write(data)


def  lin_reg():
    df = pd.read_csv(csv_link)

   

    data = df.dropna()
 
    bruh = pd.DataFrame(data)
  
    print(bruh)
    print(bruh.iloc[[-1]])
    new_high = bruh["High"].iloc[-1]
    new_low = bruh["Low"].iloc[-1]
   

    High=pd.DataFrame(data['High'])
    Low=pd.DataFrame(data['Low'])
    lm = linear_model.LinearRegression()
    model = lm.fit(High, Low)
    import numpy as np

    High_new=np.array([float(new_high)])
    Low_new=np.array([float(new_low)])
    High_new = High_new.reshape(-1,1)
    Low_new = Low_new.reshape(-1,1)
    High_predict=model.predict(High_new)
    Low_predict=model.predict(Low_new)
    print("Predicted High: ")
    print(High_predict)
    print("Predicted Low: ")
    print(Low_predict)
    print("Model Score: ")
    print(model.score(High, Low)) 
    print("Dollar Change($)")
    print((High_predict - Low_predict).astype(float))


    

df = pd.read_csv(csv_link)

data = df.dropna()

bruh = pd.DataFrame(data)

new_high = bruh["High"].iloc[-1]
new_low = bruh["Low"].iloc[-1]
High=pd.DataFrame(data['High'])
Low=pd.DataFrame(data['Low'])
lm = linear_model.LinearRegression()
model = lm.fit(High, Low)
import numpy as np
High_new=np.array([float(new_high)])
Low_new=np.array([float(new_low)])
High_new = High_new.reshape(-1,1)
Low_new = Low_new.reshape(-1,1)
High_predict=model.predict(High_new)
Low_predict=model.predict(Low_new)


try:
    lin_reg()
    

except:
    pass
import csv

from datetime import date, datetime, timedelta
today = datetime.today()
tommorow = date.today() + timedelta(days=day_num)
print(today)
print(tommorow)

header = ['date' ,'high','low','close','adj_close','volume',]
High_predict = bruh["High"].iloc[-1]
Low_predict = bruh["Low"].iloc[-1]
with open('values.csv', 'a', encoding='UTF8', newline='') as not_f:
    writer = csv.writer(not_f)
    writer.writerow('')
  
    for i in range(0,day_num):
        print(High_predict)
        
        tommorow = date.today() + timedelta(days=day_num)
        

        bruh.iloc[-1, df.columns.get_loc('Date')] = tommorow
        bruh.iloc[-1, df.columns.get_loc('High')] = float(High_predict)
        bruh.iloc[-1, df.columns.get_loc('Low')] = float(Low_predict)
        

        writer.writerow(bruh.iloc[-1])
        
        import pandas as pd
        
        
        df = pd.read_csv('values.csv')

    

        data = df.dropna()
    
        bruh = pd.DataFrame(data)
      
        new_high = High_predict
        new_low = Low_predict
       

        High=pd.DataFrame(data['High'])
        Low=pd.DataFrame(data['Low'])
        lm = linear_model.LinearRegression()
        model = lm.fit(High, Low)
        import numpy as np

        High_new=np.array([float(new_high)])
        Low_new=np.array([float(new_low)])
        High_new = High_new.reshape(-1,1)
        Low_new = Low_new.reshape(-1,1)
        High_predict=model.predict(High_new)
        Low_predict=model.predict(Low_new)
        
        day_num = day_num + 1
    
    
