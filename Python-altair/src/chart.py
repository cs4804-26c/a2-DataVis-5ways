import altair as alt
import pandas as pd

df = pd.read_csv('../../penglings.csv')

df = df.dropna(subset=['flipper_length_mm', 'body_mass_g', 'bill_length_mm', 'species'])

chart = alt.Chart(df).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm:Q',
            scale=alt.Scale(zero=False),
            title='Flipper Length (mm)'),

    y=alt.Y('body_mass_g:Q',
            scale=alt.Scale(zero=False),
            title='Body Mass (g)'),

    color=alt.Color('species:N',
                    scale=alt.Scale(domain=['Adelie', 'Chinstrap', 'Gentoo'],
                                    range=['#E57C58', '#353A4C', '#9C74B5'])),

    size=alt.Size('bill_length_mm:Q', title='Bill Length (mm)'),

    tooltip=['species', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm']
).properties(
    width=800,
    height=500
).interactive()



json_spec = chart.to_json()
html_content = f"""
<!DOCTYPE html>
<html>
<head>
  <title>Centered Altair Chart</title>
  <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
  <style>
    body {{
      margin: 0;
      height: 100vh;            
      display: flex;            
      justify-content: center;  
      align-items: center;      
      background-color: #F5F7FA; 
    }}
    #vis {{
      box-shadow: 0 4px 15px rgba(0,0,0,0.1);
      background-color: white;
      padding: 20px;
      border-radius: 8px;
    }}
  </style>
</head>
<body>
  <div id="vis"></div>
  <script type="text/javascript">
    var spec = {json_spec};
    vegaEmbed('#vis', spec);
  </script>
</body>
</html>
"""
with open('index.html', 'w')  as f:
    f.write(html_content)
print("Chart saved to python-altair/index.html ")
