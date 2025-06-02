import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# pip install openpyxl

# Load 2nd sheet from lights Excel file using pandas
data = pd.read_excel('ALAN_VIIRS_CONUS_1-20250524_210905/ALAN_VIIRS_CONUS_2012_to_2020_census_tract_level.xlsx',
                     sheet_name='2010_boundary_ALAN_2012_to_2020')

#print(data.head(2))

# List of target states
states = ['California', 'Washington', 'Oregon', 'Alaska', 'Hawaii', 'Minnesota', 'Michigan', 'Virginia', 'Maryland', 'Delaware', 'New Jersey', 'New York',
          'Connecticut', 'Rhode Island', 'Massachusetts', 'New Hampshire', 'Maine', 'Vermont', 'Colorado', 'Utah', 'Nevada']

# Use dictionary to define region mapping
region = {
    'California': 'West', 'Washington': 'West', 'Oregon': 'West', 'Alaska': 'West', 'Hawaii': 'West', 'Colorado': 'West', 'Utah': 'West', 'Nevada': 'West',

    'Minnesota': 'Midwest', 'Michigan': 'Midwest',

    'Virginia': 'East', 'Maryland': 'East', 'Delaware': 'East', 'New Jersey': 'East', 'New York': 'East', 'Connecticut': 'East', 'Rhode Island': 'East',
    'Massachusetts': 'East', 'New Hampshire': 'East', 'Maine': 'East', 'Vermont': 'East'
}

# Filter by target states
filtered = data[data['state'].isin(states)].copy()
filtered.loc[:, 'year'] = filtered['year'].astype(int)

# Assign region by mapping states using dictionary
filtered['region'] = filtered['state'].map(region)

# Group by region and year
regionData = filtered.groupby(['region', 'year'])['rad_mean'].mean().reset_index()
stateData = filtered.groupby(['state', 'year', 'region'])['rad_mean'].mean().reset_index()

# Plotting mean radiance by region
plt.figure(figsize=(12, 6))
sns.lineplot(data=regionData, x='year', y='rad_mean', hue='region', marker='o')
plt.title('Mean Radiance Over Time by Region (2012–2020)')
plt.ylabel('Radiance (nanowatt per steradian per cm²)')
plt.xlabel('Year')
plt.grid(True)
plt.legend(title='Region')
plt.tight_layout()
plt.show()

# Filter states by region for plotting
westData = stateData[stateData['region'] == 'West']
eastData = stateData[stateData['region'] == 'East']
midwestData = stateData[stateData['region'] == 'Midwest']

# Plotting mean radiance by state in each region
plt.figure(figsize=(10, 6))
sns.lineplot(data=westData, x='year', y='rad_mean', hue='state', marker='o')
plt.title('Mean Radiance in Western States (2012–2020)')
plt.ylabel('Radiance (nW/sr/cm²)')
plt.xlabel('Year')
plt.grid(True)
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=eastData, x='year', y='rad_mean', hue='state', marker='o')
plt.title('Mean Radiance in Eastern States (2012–2020)')
plt.ylabel('Radiance (nW/sr/cm²)')
plt.xlabel('Year')
plt.grid(True)
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=midwestData, x='year', y='rad_mean', hue='state', marker='o')
plt.title('Mean Radiance in Midwestern States (2012–2020)')
plt.ylabel('Radiance (nW/sr/cm²)')
plt.xlabel('Year')
plt.grid(True)
plt.legend(title='State', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()