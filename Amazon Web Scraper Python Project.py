#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
import re

import smtplib


# In[2]:


#connect to website
URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='apex_desktop').get_text()


print(title)
print(price)


# In[3]:


title = title.strip()
print(title)
price_result = re.sub('[\W_]+','.', price)
price_result1 = price_result[7:12]
print(price_result1)


# In[4]:


import datetime

today = datetime.date.today()
print(today)


# In[6]:



import csv

header = ['Title','Price','Date']
data = [title, price_result1, today]

type(data)


with open('Amazonwebscraperdataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    
    


# In[7]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Esther\Amazonwebscraperdataset.csv')
print(df)



# In[8]:


#append data to csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[10]:


#combine everything into a function
def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(id='apex_desktop').get_text()
    title = title.strip()
    
    price_result = re.sub('[\W_]+','.', price)
    price_result1 = price_result[7:12]
 
    
    import datetime

    today = datetime.date.today()
    
    
    import csv

    header = ['Title','Price','Date']
    data = [title, price_result1, today]
    with open('Amazonwebscraperdataset.csv','a+',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)


# In[ ]:


while(True):
    check_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Esther\Amazonwebscraperdataset.csv')
print(df)


# In[ ]:


#sending myself an email
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('esthermaina3000@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Esther, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'esthermaina3000@gmail.com',
        msg
     
    )

