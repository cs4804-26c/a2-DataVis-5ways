
import altair as alt
import pandas as pd

#load the data set
df = pd.read_csv("penglings.csv")
#resource for making a scatterplot
#https://altair-viz.github.io/gallery/scatter_tooltips.html
#https://altair-viz.github.io/user_guide/customization.html
#https://altair-viz.github.io/user_guide/generated/channels/altair.Size.html
#https://altair-viz.github.io/user_guide/generated/core/altair.Axis.html

chart = alt.Chart(df).mark_circle().encode(
    alt.X("flipper_length_mm", axis=alt.Axis(values = [170, 180, 190, 200, 210, 220, 230])).scale(zero=False).title("Flipper length (mm)"), #add the x axis, title, tick mark values
    alt.Y("body_mass_g", axis=alt.Axis(values = [3000, 4000, 5000, 6000])).scale(zero=False).title("Body mass (g)"), #add the y axis, title, tick mark values
    color = alt.Color("species", scale=alt.Scale(
        domain = ["Adelie", "Chinstrap", "Gentoo"],
        range = ["#FA9702","#B802FA","#018A75"] #make a manual color scale using pre-established hex codes
    )),
    size=alt.Size("bill_length_mm", scale=alt.Scale(range=[0,150])), #set the size of the point based on bill_length_mm
    tooltip = ["flipper_length_mm", "body_mass_g", "species", "bill_length_mm"] #add tooltip for interactivity
).interactive() #make it interactive

#save it to html
chart.save("penglings_altair.html")
