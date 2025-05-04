import pandas as pd
import matplotlib.pyplot as plt 

# gdp per capita growth (annual%)
 
df = pd.read_csv(r"C:\Users\Asus\Desktop\TERM2 [YR1]\GLOBAL ECONOMY\API_NY.GDP.PCAP.KD.ZG_DS2_en_csv_v2_159.csv")
df.columns = ['Country Name'] + list(df.columns[1:])

# povery headcount ratio 

df1 = pd.read_csv(r"C:\Users\Asus\Desktop\TERM2 [YR1]\GLOBAL ECONOMY\povertyheadcountratio.csv")
df1.columns = ['Country Name'] + list(df1.columns[1:])


#ghana gdp per capita growth 


ghana_data = df.loc[df['Country Name'] == 'Ghana']

ghana_data = ghana_data.drop(columns = ['Country Name'])

ghana_data = ghana_data.transpose()
 
ghana_data.columns = ['GDP Per Capita Growth']

ghana_data.index = pd.to_numeric(ghana_data.index)

ghana_data = ghana_data.loc[(ghana_data.index >= 2000) & (ghana_data.index <= 2023)]

# ghana poverty headcount ratio 

ghana_data_poverty = df1.loc[df1['Country Name'] == 'Ghana']

ghana_data_poverty = ghana_data_poverty.drop(columns = ['Country Name'])

ghana_data_poverty = ghana_data_poverty.transpose() 

ghana_data_poverty.columns = ['Poverty Headcount Ratio']

ghana_data_poverty.index = pd.to_numeric(ghana_data_poverty.index)

ghana_data_poverty  = ghana_data_poverty.dropna() 

#ivory coast gdp per capita growth 

ivorycoast_data = df.loc[df['Country Name'] == "Cote d'Ivoire"]

ivorycoast_data = ivorycoast_data.drop(columns = ['Country Name'])

ivorycoast_data = ivorycoast_data.transpose()
 
ivorycoast_data.columns = ['GDP Per Capita Growth']

ivorycoast_data.index = pd.to_numeric(ivorycoast_data.index)

ivorycoast_data = ivorycoast_data.loc[(ivorycoast_data.index >= 2000) & (ivorycoast_data.index <= 2023)]

#ivory coast poverty headcount ratio 

ivorycoast_data_poverty = df1.loc[df1['Country Name'] == "Cote d'Ivoire"]

ivorycoast_data_poverty = ivorycoast_data_poverty.drop(columns = ['Country Name'])

ivorycoast_data_poverty = ivorycoast_data_poverty.transpose()

ivorycoast_data_poverty.columns = ['Poverty Headcount Ratio']

ivorycoast_data_poverty.index = pd.to_numeric(ivorycoast_data_poverty.index)

ivorycoast_data_poverty = ivorycoast_data_poverty.dropna() 

#PLOTTING 

plt.plot(ghana_data.index,  ghana_data['GDP Per Capita Growth'], label = 'Ghana GDP Growth', color = 'blue')
plt.plot(ivorycoast_data.index, ivorycoast_data['GDP Per Capita Growth'], label = 'Ivory Coast GDP Growth', color = 'lightblue')

plt.plot(ghana_data_poverty.index, ghana_data_poverty['Poverty Headcount Ratio'], label = 'Ghana Poverty Ratio', color = 'red')
plt.plot(ivorycoast_data_poverty.index, ivorycoast_data_poverty['Poverty Headcount Ratio'], label = 'Ivory Coast Poverty Ratio', color = 'darkred')


plt.ylabel('GDP Per Capita Growth (Annual%) / Poverty Ratio (%)')
plt.xlabel('Years')
plt.title("GDP Per Capita Growth/ Poverty Headcount Ratio \n of Ghana and Ivory Coast [2000-2023]")
plt.xticks(range(2000, 2023, 5))

plt.legend() 



plt.grid(True)
plt.show() 

