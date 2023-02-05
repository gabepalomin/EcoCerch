import matplotlib.pyplot as plt

## Import seaborn
import seaborn as sns
import pandas as pdt
# Apply the default theme
sns.set_theme()

# Load an example dataset
#snak = sns.load_dataset("Co2_emissions.csv")
snak2 = pdt.read_csv("Co2_emissions.csv")
#agri_land = pdt.read_csv(r"C:\Users\johan\Downloads\johanna_agricultural_land_per_capita.csv")
snak2.head()
g4 = sns.barplot(
     data = snak2, x="Year", y="Annual CO2 emissions (per capita)",
)
g4.set(xticklabels=[])  
g4.set(title='Annual CO2 emissions in the US from 1850-2020 (per capita)')
g4.set(xlabel=None)  # remove the y-axis label
g4.tick_params(left=False)

#plt.savefig('output.png')


plt.show() 

agri_land = pdt.read_csv("agricultural_land_per_capita.csv")
agri_land.head()
g2 = sns.barplot(
     data = agri_land, x= "Year", y= "Agricultural Land per Capita",
     
)
g2.set(xticklabels=[])  
g2.set(title='Agricultural Land per Capita: 1960-2020')
g2.set(xlabel=None)  # remove the y-axis label
g2.tick_params(left=False)

#plt.savefig('output2.png')

g3 = sns.relplot(
    data=agri_land, kind = "line",
    x="Year", y="Agricultural Land per Capita", alpha = 0.5,height=3,
   
    facet_kws=dict(sharex=False),
)
g3.set(title='Agricultural Land per Capita: 1960-2020')

#plt.savefig('output3.png')
plt.show() 


