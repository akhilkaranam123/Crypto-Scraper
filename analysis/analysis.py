from matplotlib import pyplot as plt
import seaborn as sns

#Find the outliers for Bitcoin Prices

sns.boxplot(df_bitcoin['Close'])

#Find the ouliers for Ethereum Prices

sns.boxplot(df_ethereum['Close'])


#Analysis of Patter for Bitcoin

date_time = df_bitcoin['Date']
data = df_bitcoin['Close']

DF = pd.DataFrame()
DF['value'] = data
DF = DF.set_index(date_time)
plt.plot(DF)
plt.gcf().autofmt_xdate()
plt.show()

#Analysis of Patter for Ethereum

date_time = df_ethereum['Date']
data = df_ethereum['Close']

DF = pd.DataFrame()
DF['value'] = data
DF = DF.set_index(date_time)
plt.plot(DF)
plt.gcf().autofmt_xdate()
plt.show()





