import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



beer = pd.read_csv('C:\\Users\\user\\.spyder-py3\\beer\\beers.csv')
brew = pd.read_csv('C:\\Users\\user\\.spyder-py3\\beer\\breweries.csv')

#SEE IF NaN VALUES EXISTS
print(beer.isna().any())

print(beer.info())
print(beer.head())
print(beer.dtypes)
print(beer.describe())


sns.distplot(beer["abv"])
plt.xlabel("Alcohol By Volume")
plt.show()



#BAR GRAPH OF MOST BREWED BEER STYLES
plot3 = beer.groupby('style')['name'].count().nlargest(15).plot(kind='bar', \
               title='Most Brewed Beer Styles', \
               colormap='summer',  )

plot3.set_ylabel('Number of Different Beers')





#%%

#BAR GRAPH OF NUMBER OF BREWERIES IN EACH STATE
plot = brew.state.value_counts().plot(kind='bar', title="Number of Breweries in Each State", \
                             figsize=(8,6), colormap='summer')
plot.set_xlabel('State')
plot.set_ylabel('Number of Breweries')
mean_line = plot.axhline(brew.state.value_counts().mean(), color='r',\
                         label='Average Number of Breweries')
plt.legend()


#BAR GRAPH OF CITIES WITH MOST BREWERIES
plot5 = brew.groupby('city')['name'].count().nlargest(15).plot(kind='bar', \
               title='Cities with the Most Breweries', \
               colormap='summer',  )
plot5.set_ylabel('Number of Breweries')


#%%


temp = beer.groupby('abv')["name"].count().sort_values(ascending=False).head(50)

#Craft Beers Alcohol content
x = list(temp.index.values)
for i in range(len(x)):
    x[i] = np.format_float_positional(np.float16(x[i]*100))
y = temp.values

fig_size = plt.rcParams["figure.figsize"]
# Set figure width to 12 and height to 9
fig_size[0] = 27
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size
sns.barplot(x,y)
plt.xlabel("Alcohol Volume (%)",color='green')
plt.ylabel("Number of Beers",color='green')
plt.title("Craft Beer by Alcohol content", color='blue')
plt.show()


#%%



beertemp = beer
beertemp.dropna(inplace=True)
sns.lmplot("ibu","abv", data=beertemp,markers="x")
plt.xlabel("Bitterness (ibu)",color='blue')
plt.ylabel("Absolute Volume (abv) - Alcohol Content",color='blue')
plt.title("Craft Beers -- Bitterness vs Alcohol Content ", color='#BE823A')




#%%

beer['style'].value_counts()[:15].plot(kind = "bar", color = "red")

plt.title("Most Common Beer Styles")


#%%

sns.countplot(data=beer,y='ounces')


plt.figure(figsize=(14,14))
sns.countplot(data=brew,y='state')



















