import pandas as pd

df=pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")


pd.set_option("display.max_columns", 999)
new_df=df[['Mortality rate, infant (per 1,000 live births)','GDP per capita (constant 2010 US$)', 'Country Name']]


from plotnine import *
(ggplot(new_df , aes(x='Mortality rate, infant (per 1,000 live births)', y='GDP per capita (constant 2010 US$)')) + geom_point())
