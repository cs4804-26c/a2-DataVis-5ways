Code, visualization images and files can be found in their respective folders of this repo.

Also link to D3 visualization: https://anthonyrcoutts.github.io/a2-CS4084-AnthonyCoutts/scatterrug.html

# R + ggplot2 + dyplr (also RColorBrewer and scales for colors)
R is a programming language primarily used for statistical techniques, data manipulation and data visualizations. It is relatively easy to acess by simply downloading R and R studio (or another IDE) on to your device. It does require programming and coding knowledge specifically coding in R.

To build the visualization, I first filtered out null values and made sure columns were set to the proper type using dyplr. From there I created a ggplot using geom_point, setting flipper length as the x axis, body mass as the y axes, species as the color and bill length as the size in the aesthetics. After that I changed the x and y axis ranges and their labels. FInally, I changed the colors of the species to match the original visualization.

Fortunately, I have a pretty strong background in R and specifically using ggplot to build visualizations so, this wasn't very difficult for me. That said, I can see how someone not experienced with R and ggplot may struggle at first to put together a plot like this. That said, there are plenty of resources and videos to help guide someone. R and ggplot make it easy to make the plot customizeable and easy to change small details like the plot background, colors, legend position and many more customizations. Overall, R and ggplot allows for highly customizeable visualization and becomes easy to use after some practice.

<img width="1119" height="683" alt="Rplot" src="https://github.com/user-attachments/assets/f51f30e8-ec06-4069-89ce-6e41238c6ef9" />


# d3

D3 is a powerful library to build dynamic and creative visualizations. It is relatively easy to access by simply installing JS and an IDE on to your machine. That said, it does require significant programming knowledge in JS and html. It also takes some time to learn the D3 syntax and how it works with things like data loading.

To build this visualization I set the visualization's dimensions and margins as well as a space for it to go on the web page. Then I loaded the data in and cleaned it by filtering out missing values. Then I created the svg. From there a created the linear scales for the x and y axis as well as the size scale. Then I specified the color pallete to match the original visualization and set up the legends for size and color on the right side. Then I added the axes using the x and y scales created before and created a grey background grid with white tick lines to match the original visualization. Finally, added the dots using the x, y, size and color scales created before.

The process of building this visualization did take awhile for me. I have little experience with D3 so I had to learn a lot to put things together like loading in the data. That said, there are plenty of example plots which can be used to help guide people to build their own visualizations. D3 is highly customizeable which is one of its main advantages. Features can be placed anywhere with ease, aesthetics are easily defined and scales are easily manipulated. Overall, D3 is a powerful tool, expecially for building interactive and custom visualizations.

<img width="1545" height="907" alt="D3 Plot" src="https://github.com/user-attachments/assets/7b7ca7b5-e425-4d1c-9296-251c7398edcd" />


# Python + Seaborn + Matplotlib

Python and its libraries seaborn and matplotlib are fiarly popular selections for data visualizations. Python has a relatively ease of access by installing python and an IDE to your machine. Python is also known as a more beginner friendly language but does require programming skills nonetheless.

Tp build the visualization I read in the data and set the color pallete to match the original version. I set the figure size and used seaborn to plot the data, assigning flipper length as the x variable, body mass as the y variable, species as the hue and bill length as the size. From there a set some minor features to match the visualization such as the grey background with white tick lines, legend location and x and y labels and limits.

The recreation of the original visualization was pretty simple in python and its libraries. The small features like the plot background were easy to customize. Python seems like it strikes a good balance between a beginner freindly visualization tool and ability to customize visuals. One critic would be that the size of the dots isn't very different.

<img width="588" height="331" alt="plot" src="https://github.com/user-attachments/assets/2dc4bbe7-e73a-433d-a254-16dd2e7ecb88" />


# Flourish

Flourish is another visualization platfrom that has gained popularity recently for its ease of use and access. Flourish allows users to build a wide range of visualizations right in the browser with free accounts, making it easy to access and create visualizations. It is a GUI environment that requires no coding knowledge or experience to build visualizations.

To build the visualization, I specified flipper length as the x variable, body mass as the y variable, species as the color variable and bill length as the size variable in the data tab. I then went to the visualization and the colors tab to change the colors, plot background tab to change the background color and tick lines. I then went to each axis to rename the axes.

Originally, the process of rebuilding the visualization was pretty simple. However, Floursih struggled with some very simple customizations and key elements in teh visualization. First, I was unable to find a way to move the legend to the correct location and furthermore, it would not generate a legend for the sizing. These are huge drawbacks as these are simple elements that should be easy to customize. Additionally, the size scaling of the dots makes it hard to decifer the difference between small and large bill lengths. Some settings are also just hard to find. Flourish is very accesbile and cretaes simple visualizations easily but further customization past basic customization in Flourish is hard or impossible leaving an inability to create some more complex or nuanced visualizations.

<img width="1127" height="686" alt="CS4804 DataVis" src="https://github.com/user-attachments/assets/f24513bf-837c-483d-a915-71cd0e4a80a1" />


# Tableau

Tableau is a data visualization platform that has gained popularity specifically within the business sector. Tableau is known for being able to build dashboards to display a variety of data visualizations. Tableau is popular for its ease of use in creating simple visualizations. To create visualizations you can drag and drop features to the desired axis/visual channel and Tableau generate the visualization for you. It is a GUI environment which requires no coding to generate visualizations which is one of the reasons for its popularity.

To recreate the visualizations in Tableau I dragged flipper length to the x axis and body mass to the y axis, setting both to "dimension" to get a scatter plot. Then I dragged species to the color channel and bill length to the size channel. Finally, I renamed the axes and set the background color to grey, tick lines to white and the colors to match the visualization.

While Tableau was fairly easy to recreate the visualization, I did have some struggles. First changing the background of the figure was not the easy to find. Also the size scaling of the dots makes it hard to tell the difference between smaller bill lengths and larger ones, and I couldn't find a way to fix this. Tableau does a great job creating simple visualizations for users without much coding background but struggles to allow users make smaller and nuanced customizations like changing the size scaling and background. Overall, I'd say Tableau has a low barrier to entry and excels at building simple visualizations for users with little coding background however, it struggles to make more advanced visualizations and may not be as useful for users with a strong coding background.

<img width="1433" height="772" alt="Tableau Plot" src="https://github.com/user-attachments/assets/6bb67f37-faaa-4362-89d9-de5f0f35b116" />


## Technical Achievements

For this assignment I turned the D3 visualization into an interactive visualization (see Enhanced Visualization tab on github pages url). In my visualization you can click on the data point of a given species and it will lower the transparency of the other data points not in that group. You can also click the legend to get the same effect of highlighting a specific group. I also added a rug plot to the bottom which can also be clicked and produce the same effect. To return the highlighting back to normal simply click anywhere on the background or click another data point to highlight a different group. This achievement allows users to better inspect the data of different species. I did this by creating a function that can be used in the.on("click"...) part of the data and legend that will increase the opacity of the selected group and decrease the opacity of the other groups in a smooth transition. I also changed the pointer when hovering over data and the legend to indicate to the user that you can click them.

Unhighlighted:
<img width="1667" height="920" alt="Enhanced Visual no click" src="https://github.com/user-attachments/assets/7bf74d1a-424f-48ce-94c8-e8d83307a54c" />

Highlighted:
<img width="1540" height="917" alt="Enhanced Visual click" src="https://github.com/user-attachments/assets/c46a6da5-5432-477f-bc15-b042f7985420" />



Additionally, I animated the r ggplot into a gif that cycles through the groups. Once again, this allows users to see groups stand alone and then compare them together. To do this I used the gganimate package and the transition_states function, setting the transition to be the species.

Gif:
![r_anim](https://github.com/user-attachments/assets/c9fd585d-1d80-4a20-8e54-d8f6fec98f8a)


## Design Achievements

For the design achievement I added a rug plot for the x and y axes of the D3 visualization that allows users to better see the distribution of the data by species. This makes it so not only overalll trends amooung all species are shown but also the distribution of data amoungst each species. The rugs were created using a rectangle on the x and y axis to house the rugs. Then, lines were used to build the rugs using filtered data for that one species on the given axis. The rugs were staggered by species to clearly see the distribution for each species. Additionally, I changed the color pallete and got rid of the grey background so the data can be better seen and the differences are clearer. I used: http://vrl.cs.brown.edu/color to generate my color pallete.

Visualization with rug plots:
<img width="1667" height="920" alt="Enhanced Visual no click" src="https://github.com/user-attachments/assets/a3dce03e-fdf0-42be-b70a-f0bec829d453" />


Inspiration for the design:
<img width="550" height="430" alt="image" src="https://github.com/user-attachments/assets/22a48ce3-cd57-4b61-8c6f-36765c2081c0" />


I also made some small styling changes to the animated ggplot.

# Code used from outside sources to start
https://observablehq.com/@d3/scatterplot-with-shapes

