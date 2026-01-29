import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('../penglings.csv')

# Drop rows with missing values
data = data.dropna()

species_order = ['Adelie', 'Chinstrap', 'Gentoo']
species_palette = {
	'Adelie': 'orange',
	'Chinstrap': '#A550EF',
	'Gentoo': 'darkcyan',
}

def create_scatterplot():
	sns.set_theme(style="darkgrid")
	fig, ax = plt.subplots(figsize=(10, 6))
	ax = sns.scatterplot(
		data=data,
		x='flipper_length_mm',
		y='body_mass_g',
		hue='species',
		hue_order=species_order,
		palette=species_palette,
		size='bill_length_mm',
		sizes=(60, 300),
		alpha=0.8,
		ax=ax,
	)

	# Match edge color to face color to match ggplot2 style
	for c in ax.collections:
		c.set_edgecolor(c.get_facecolor())

	# AI Usage Note: Can you make the legend appear to the right of the plot, not covering any points?

	plt.xlabel('Flipper Length (mm)')
	plt.ylabel('Body Mass (g)')
	ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
	fig.tight_layout(rect=(0, 0, 1, 1))
	plt.savefig('../img/matplotlib-scatterplot.png', dpi=300)

def create_scatterplot_3d(save=True):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111, projection='3d')

	for species in species_order:
		subset = data[data['species'] == species]
		ax.scatter(
			subset['flipper_length_mm'],
			subset['body_mass_g'],
			subset['bill_length_mm'],
			color=species_palette[species],
			label=species,
			s=60,
			alpha=0.8
		)

	ax.set_xlabel('Flipper Length (mm)')
	ax.set_ylabel('Body Mass (g)')
	ax.set_zlabel('Bill Length (mm)')

	ax.legend(title='species', bbox_to_anchor=(1.02, 1), loc='upper left')
	
	if save:
		plt.savefig('../img/matplotlib-scatterplot-3d.png', dpi=300)
	else:
		plt.show()

if __name__ == "__main__":
	create_scatterplot_3d()
	create_scatterplot()