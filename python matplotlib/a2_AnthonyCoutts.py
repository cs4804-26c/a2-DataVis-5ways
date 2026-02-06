# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 22:25:08 2026

@author: antho
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

penglings = pd.read_csv("penglings.csv")

palette = {
    "Gentoo": "#1B9E77",
    "Adelie": "#D95F02",  
    "Chinstrap": "#7570B3"    
}

plt.figure(figsize=(7, 5))
sns.scatterplot(data=penglings, x="flipper_length_mm", y="body_mass_g",
                hue="species", size="bill_length_mm", palette=palette, alpha = 0.8)
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.ylim(2500, 6500)
plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc="upper left",
    borderaxespad=0
)
sns.set_theme(style="whitegrid")
ax = plt.gca()
ax.grid(
    True,
    which="both",
    color="white",
    linewidth=1
)
ax.set_facecolor("#d1d1d1") 
plt.show()