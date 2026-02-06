# !pip install altair

import altair as alt
import pandas as pd

penglings = pd.read_csv("../penglings.csv")

chart = (alt.Chart(penglings).mark_circle(opacity=0.8).encode(x=alt.X("flipper_length_mm",
                                                                      scale=alt.Scale(domainMin=170),
                                                                      title="Flipper Length (mm)"),
                                                              y=alt.Y("body_mass_g",
                                                                      scale=alt.Scale(domainMin=2500),
                                                                      title="Body Mass (g)"),
                                                              color=alt.Color("species",scale=alt.Scale(domain=["Adelie", "Chinstrap", "Gentoo"],
                                                                                                        range=["orange", "purple", "blue"])),
                                                              size="bill_length_mm")
                                                            .properties(title="Penguin Size by Species"))

chart
