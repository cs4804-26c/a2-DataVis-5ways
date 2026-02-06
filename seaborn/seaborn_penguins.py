import pandas as pd
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../penglings.csv').dropna()
palette = {'Adelie': '#E8862A', 'Chinstrap': '#9B59B6', 'Gentoo': '#2E9E8F'}

fig, ax = plt.subplots(figsize=(10, 7))
sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g',
                hue='species', size='bill_length_mm', sizes=(30, 200),
                alpha=0.8, palette=palette, edgecolor='none', ax=ax)

ax.set_xlabel('Flipper Length (mm)')
ax.set_ylabel('Body Mass (g)')
plt.tight_layout()
plt.savefig('seaborn_penguins.png', dpi=150)
