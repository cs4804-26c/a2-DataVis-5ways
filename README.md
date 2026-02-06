
![penguins](https://github.com/cs4804-24c/a2-DataVis-5Ways/assets/412089/accc5680-3c77-4d29-9502-d3ff8cd922af)

# 02-DataVis-5ways

Assignment 2 - Data Visualization, 5 Ways  
===

Now that you have successfully made a "visualization" of shapes and lines using d3, your next assignment is to successfully make a *actual visualization*... 5 times. 

The goal of this project is to gain experience with as many data visualization libraries, languages, and tools as possible.

I have provided a small dataset about penguins, `penglings.csv`.
Each row contains a penguin observation and several variables about it, including bill length, flipper length, and more.

Your goal is to use 5 different tools to make the following chart:

![](img/ggplot2.png)

These features should be preserved as much as possible in your replication:

- Data positioning: it should be a upward-trending scatterplot as shown.  Flipper Length should be on the x-axis and Body Mass on the y-axis.
- Scales: Note the scales do not start at 0.
- Axis ticks and labels: both axes are labeled and there are tick marks at a reasonable interval, e.g 10, 20, 30, etc.
- Color mapping to species.
- Size mapping to Bill Length.
- Opacity of circles set to 0.8 or similar for a semi-transparent effect.

Other features are not required. This includes:

- The background grid.
- The legends.

Note that some software packages will make it **impossible** to perfectly preserve the above requirements. 
Be sure to note where these deviate as you reflect on what a tool is good for.

Improvements are also welcome as part of Technical and Design achievements.

Libraries, Tools, Languages
---

You are required to use 5 different tools or libraries.
Of the 5 tools, you must use at least 3 libraries (libraries require code of some kind).
This could be `Python, R, Javascript`, or `Java, Javascript, Matlab` or any other combination.
Dedicated tools (i.e. Excel) do not count towards the language requirement.

Otherwise, you should seek tools and libraries to fill out your 5.

Below are a few ideas. Do not limit yourself to this list!
There are new tools coming out every year and we may not have an exhaustive list of the latest and greatest.

Some may be difficult choices, like Matlab or SPSS, which require large installations, licenses, and occasionally difficult UIs.

I have marked a few that are strongly suggested.

- R + ggplot2 `<- definitely worth trying`
- Excel
- d3 `<- since the rest of the class uses this, we're requiring it`
- Altair `<- hugely popular python library. highly recommended `
- three.js `<- well, it's a 3d library. not really recommended, but could be interesting and fun`
- p5js `<- good for playing around. not really a chart lib`
- Tableau
- PowerBI
- Vega-lite <- `<- very interesting formal visualization model; might be the future of the field`
- Flourish <- `<- popular in recent years`
- DataWrapper <- `<- popular in recent years`
- GNUplot `<- the former CS department head uses this all the time :)`
- SAS/SPSS/Matlab

You may write everything from scratch, or start with demo programs from books or the web. 
If you do start with code that you found, please identify the source of the code in your README and, most importantly, make non-trivial changes to the code to make it your own so you really learn what you're doing. 

Tips
---

- If you're using d3, key to this assignment is knowing how to load data.
You will likely use the [`d3.json` or `d3.csv` functions](https://d3js.org/d3-dsv) to load the data you found.

**Beware that these functions are *asynchronous*, meaning it's possible to "build" an empty visualization before the data actually loads. Figuring out how to do this properly can be a major hiccup if you haven't used async functions before. If this means you, start part of this project early so you don't end up in a rush!**

- *For web languages like d3* Don't forget to run a local webserver when you're debugging.
See my a1 video or online tutorials for how to do this.
Being able to host a local webserver is an essential web development skill and very common in visualization design as well.

Readme Requirements
---

A good readme with screenshots and structured documentation is required for this project. 
It should be possible to scroll through your readme to get an overview of all the tools and visualizations you produced.

- Each visualization should start with a top-level heading (e.g. `# d3`)
- Each visualization should include a screenshot. Put these in an `img` folder and link through the readme (markdown command: `![caption](img/<imgname>)`.
- Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?

Other Requirements
---

0. Your code should be forked from the GitHub repo.
1. Place all code, Excel sheets, etcetera in a named folder. For example, `r-ggplot, matlab, mathematica, excel` and so on.
2. Your writeup (readme.md in the repo) should also contain the following:

- Description of the Technical achievements you attempted with this visualization.
  - Some ideas include interaction, such as mousing over to see more detail about the point selected.
- Description of the Design achievements you attempted with this visualization.
  - Some ideas include consistent color choice, font choice, element size (e.g. the size of the circles).

GitHub Details
---

- Fork the GitHub Repository. You now have a copy associated with your username.
- Make changes to fulfill the project requirements. 
- To submit, make a [Pull Request](https://help.github.com/articles/using-pull-requests/) on the original repository.

Grading
---

Grades on a 120 point scale. 
24 points will be based on your Technical and Design achievements, as explained in your readme. 

Make sure you include the files necessary to reproduce your plots.
You should structure these in folders if helpful.
We will choose some at random to run and test.


# d3

d3 is a JavaScript visualization library. I did this by constructing an svg using information from the csv. Although, I found it annoying how much code was needed to create scales and parameters. It did feel fairly powerful and I could tell which new features I was slowly adding in. I did force some data into numbers.



![d3](img/d3_plotJY.png)

# Altair

Altair is a Python visualization library. I found it easy to create a graph with little code while mapping out factors like colors and scale. Overall, it felt good to use and I really enjoyed its capabilities for how clean the code felt compared to d3. I did force some data into numbers.


![Altair](img/altair_plotJY.png)

# Datawrapper

Datawrraper is an online visualization tool. You can upload a dataset and use it to quickly create a chart. The UI is easy to understand to modify the graphic as needs to handle many simple parameters and displays. Although I find the simplicity lacking when I want to customize the visual more finely, as I'm restrained by the site UI. No hacks or data manipulation were used.

https://datawrapper.dwcdn.net/fZBRj/2/


![Datawrapper](img/datawrapper_plotJY.png)


# Flourish

Flourish is an online visualization software. It was easy to setup up initially due to the template format, and feels like a good starting point to quickly experiment with different datasets. Although, I found the template too restricting when I wanted to optimize certain parameters more specifically. No hacks or data manipulation were used.

https://public.flourish.studio/visualisation/27521330/

![Flourish](img/flourish_plotJY.png)

# R + ggplot

ggplot is a charting libary that uses the R language. I used geom_point() to conceptualize the dataset, and added other features like opacity and color where needed. I found it okay to use like Altair and felt the code was cleaner than Altair. No hacks or data manipulation were used.

![ggplot2](img/r_ggplot2_JY.png)


## Technical Achievements
- **Added Interactivity**: For d3, you can hover over each point of data to learn more info about it.


### Design Achievements
- **Consistent Color Choice**: Maintaining a general set of regonizable colors between each plot.
- **Usage of Legends**: I attempted to have legends for all of the scatterplots to best show what each species is represented by and the general size frame to users. I was unable to get a legend for size in Flourish.

