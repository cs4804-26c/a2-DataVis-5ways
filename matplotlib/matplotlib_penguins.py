import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

df = pd.read_csv('../penglings.csv').dropna()
colors = {'Adelie': '#E8862A', 'Chinstrap': '#9B59B6', 'Gentoo': '#2E9E8F'}

fig, ax = plt.subplots(figsize=(10, 7))
for species, group in df.groupby('species'):
    ax.scatter(group['flipper_length_mm'], group['body_mass_g'],
               s=group['bill_length_mm'] * 3, c=colors[species],
               alpha=0.8, label=species, edgecolors='none')

ax.set_xlabel('Flipper Length (mm)')
ax.set_ylabel('Body Mass (g)')
ax.legend(title='Species')
plt.tight_layout()
plt.savefig('matplotlib_penguins.png', dpi=150)
