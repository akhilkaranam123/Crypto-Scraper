import seaborn as sns

sns.boxplot(df_ethereum['Close'])
sns.boxplot(df_bitcoin['Close'])
from matplotlib import pyplot as plt

sns.distplot(df_bitcoin['Close'],kde = False)
plt.show()
sns.distplot(df_ethereum['Close'],kde = False)
plt.show()






