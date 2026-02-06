import matplotlib.pyplot as plt
import pandas as pd

# Referred to https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html for reading the csv, since it's been some time (mainly regarding the additional params, which I ended up keeping default)
rawPenglingsDf = pd.read_csv("penglings.csv")
print(rawPenglingsDf)

rawPenglingsFilteredDf = rawPenglingsDf.dropna()
print(rawPenglingsFilteredDf)

# Referred to https://www.geeksforgeeks.org/python/normalize-a-column-in-pandas/ for determining which type of scaling to use for the bill length (went with min-max scaling, but multiplied the column values by a large number to amplify size differences) 
rawPenglingsFilteredDf["bill_length_mm"] = (rawPenglingsFilteredDf["bill_length_mm"] - rawPenglingsFilteredDf["bill_length_mm"].min()) / (rawPenglingsFilteredDf["bill_length_mm"].max() - rawPenglingsFilteredDf["bill_length_mm"].min()) * 200
print(rawPenglingsFilteredDf)

onlyAdelieDf = rawPenglingsFilteredDf[rawPenglingsFilteredDf["species"] == "Adelie"]
onlyChinstrapDf = rawPenglingsFilteredDf[rawPenglingsFilteredDf["species"] == "Chinstrap"]
onlyGentooDf = rawPenglingsFilteredDf[rawPenglingsFilteredDf["species"] == "Gentoo"]

print(onlyAdelieDf)
print(onlyChinstrapDf)
print(onlyGentooDf)

# Referred to https://www.w3schools.com/python/matplotlib_scatter.asp for making sure I was properly using plt.scatter (mainly in terms of data input)
# Also referred to https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html for a refresher on all the params/attributes of plt.scatter
# Referred to https://www.geeksforgeeks.org/python/how-to-add-a-legend-to-a-scatter-plot-in-matplotlib/ for creating the legend
plt.scatter(onlyAdelieDf["flipper_length_mm"], onlyAdelieDf["body_mass_g"], s = onlyAdelieDf["bill_length_mm"], c = "orange", alpha = 0.8, label = "Adelie")
plt.scatter(onlyChinstrapDf["flipper_length_mm"], onlyChinstrapDf["body_mass_g"], s = onlyChinstrapDf["bill_length_mm"], c = "#ba55d3", alpha = 0.8, label = "Chinstrap")
plt.scatter(onlyGentooDf["flipper_length_mm"], onlyGentooDf["body_mass_g"], s = onlyGentooDf["bill_length_mm"], c = "teal", alpha = 0.8, label = "Gentoo")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.legend()
plt.show()
