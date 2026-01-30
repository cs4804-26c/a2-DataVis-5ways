import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

#load the csv
df = pd.read_csv('../penglings.csv')

#define colors for the species.
species_colors = {
    'Adelie': 'orange',
    'Chinstrap': 'purple',
    'Gentoo': 'teal'
}

#create a scatter plot for each species
fig, ax = plt.subplots(figsize=(9, 4.5))
for species, group in df.groupby('species'):
    ax.scatter(group['flipper_length_mm'], 
               group['body_mass_g'], 
               s=group['bill_length_mm'] / 2, # Size of the marker
               c=species_colors[species], 
               label=species, 
               alpha=0.6, 
               edgecolors='w')

#set the title and labels
ax.set_title('Penguin Size by Species')
ax.set_xlabel('Flipper Length (mm)')
ax.set_ylabel('Body Mass (g)')

#create a legend!
legend_elements = [Line2D([0], [0], marker='o', color='w', label=species,
                          markerfacecolor=color, markersize=10)
                   for species, color in species_colors.items()]
ax.legend(handles=legend_elements, title='Species')

#show the plot :)
plt.show()