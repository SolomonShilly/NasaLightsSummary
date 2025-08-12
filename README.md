## NasaLightsSummary

### Required Installations:
- openpyxl
- seaborn
- matplotlib
- pandas

### Data Source:
- Annual Summary of Artificial Light At Night from VIIRS/S-NPP
- https://search.earthdata.nasa.gov/search/granules?p=C2650219940-GES_DISC&q=lights%20at%20night&fst0=Atmosphere&lat=35&long=-92.71553112271542&zoom=2.9438568133858167
- To learn more about VIIRS/S-NPP, read https://snow.nasa.gov/missions/s-npp-viirs

### Results:
- Using IPUMS data from 2019 -2023, I was able to create a Tableau map of states based on avaerage household incomes (Available at https://github.com/SolomonShilly/Tableau-Visualizations/blob/main/States_HHINCOME.twb)
- This led me to wondering whether coastal cities in the US had more activity than midwestern states due to a large majority of coastal states having higher median incomes than Midwestern states
- Based on the data, Eastern and Western states had significantly more lights than Midwestern states on average between 2012 - 2020
- States with median incomes greater than $110,000 exhibited more light than states with a median income less than $110,000
- Nevada, New York, New Jersey, California, and Maryland had the highest average radiance between 2012 - 2020
- Nevada was the outlier. Nevada had a median income lower than $110,000, but had the highest average radiance
