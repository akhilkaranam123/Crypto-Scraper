import pandas as pd
import s3_connection
pd.set_option('display.float_format', '{:.2f}'.format)
import requests
from bs4 import BeautifulSoup
import seaborn as sns
from datetime import datetime
import sys

#Crypto_Scrape function to scrape data from coingecko website. We can give the Crypto currency as arguments and also the filename and filepath to upload to s3

def crypto_scrape(currency_name,filename,filepath):
    try:
        url = 'https://www.coingecko.com/en/coins/'+currency_name.lower()+'/historical_data#panel'
        webpage = requests.get(url)
        soup = BeautifulSoup(webpage.text, 'html.parser')
        names = []
        name = soup.find_all('th',{'class':'text-center'})
        for i in range(5):
            names.append(name[i].get_text())
        table1 = soup.find_all('td')
        x = [table1[i:i + 4] for i in range(0, len(l), 4)]
        price1,price2 = [],[]
        for i in table1:
            price1.append(i.get_text().split('\n')[1])
        for i in range(4,len(price1)):
            price1[i] = round(float(price1[i].split('$')[1].replace(',','')),2)
        price1 = price1[4:]
        x = [price1[i:i + 4] for i in range(0, len(price1), 4)]
        df = pd.DataFrame(x,columns = names[1:])
        df['Close'].mean()
        df['Open'].mean()
        th = soup.find_all('th',attrs={'scope':'row'})
        Day = []
        for i in th:
            Day.append(datetime.strptime(i.get_text(),'%Y-%m-%d').date())
        df['Date'] = Day[1:]
        upload_s3(filename,filepath)
    except:
        print('Currency name is not right')
        raise

if __name__ == '__main__':
    crypto_scrape(currency_name,filename,filepath)

