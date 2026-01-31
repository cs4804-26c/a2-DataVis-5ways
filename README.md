# Assignment 2 : 5-Way Visualizations
By Skyler Dooley
02/06/2026
---
# Altair (Python)
Altair was pretty straightforward and easy to use and understand. It is concise and decorative, but size scaling is less intuitive than ggplot2. The amount of code needed to achieve the visual was very minimal, especially since it uses python which I am very familiar with. I really enjoyed using this tool to create the visualization because I was able to quickly go into the code itself and see exactly what I needed to change or add to alter the visual. There was a slight learning curve since I was not familiar with Altair itself, but after some research it was pretty straightforward. I can see this tool being useful in the future to create a quick and simple visual with any size data set. It was very easy to specify each individual variable along with their own customizations (scale, color label) since all the code was very short and right to the point. I would use this tool in the future if I needed to create a visual quickly and without a lot of effort.

![altair image](/img/altair.png)

---
# d3 (Javascript)
d3 was much more lengthy process than Altair, mainly because it was using Javascript, but the functions themselves were repetative so once I understood a few of the basic functions it was a fairly quick process to go through the rest. There was not as much of a learning curve since we had used d3 in assignment 1, so I was able to use my basic knowledge to get started. There was a lot of code required to create the visual (in comparison to Altair), but it did allow me to make a lot of specific customizations to every aspect of the visual. I can see this tool being used in the future for any size dataset that requires a lot of specifications and customizations to the vsualization, while also keeping in mind that it would take more time to create this visual if coding from scratch. If someone was not already familiar with java and d3, there would be a bit of a drastic learning curve, but it would be worth it to take the time to learn how to use this tool due to its ability to make very customizable visuals. I would use this tool if Altair was not able to meet the needs of the visual. 

![d3 image](/img/d3.png)

---
# R + ggplot2 (R)
Similiarly to Altair, this tool did not require a lot of code to be written, but it does require some basic knowledge about how to use R. This tool is very good at creating precise visualizations regardless of the size of the dataset, but there is a learning curve and the language itself is very different to most other coding languages. However, I believe that this tool is great if someone wants to create a specific visual and does not have a large amount (or any) coding experience, given that this tool is used in some math classes at WPI. I personally do not prefer using R and ggplot because the language itself is very specific and easy to make mistakes. This tool could be useful in a more math-based scenario that requires a quickly created visual with specific scaling.

![ggplot image](/img/ggplot.png)

---
# Excel
Initially I thought that the excel implementation would be the easiest, but it proved to be extremely tedious. A large majority of the work done in excel had to be done manually; I had to add the axis/chart titles, legend titles, colors, and the bill_length_nm lengend in its entirety. To make the bill_length legend, I created circles of different sizes and added in a text box with the header and placed it on top of species in the legend area. It is difficult to make small alterations to excel charts, which made this process much longer than it should have been. I also had to manually select each column and range where each data value was being read from. It was easy to have the chart type already defined instead of creating it from scratch, but adding in the data itself was difficult and time consuming. In the past I have prefered to use excel, but that was on small datasets with only 2-3 variables, whereas this visual had 4 variables. I could see excel being useful if you need to make a quick comparison of 2-3 values/variables in a dataset of any size (though it is easier to use on smaller datasets). In the end, I would not use excel again to create a complex chart like this again (this was such a painful process). 

![excel image](/img/excel.png)

---
# PowerBI
I had never used PowerBi before but I was familiar with Tableau. I found this tool extremely easy and quick to use and understand. This was by far the fastest tool that I used from starting the tool to getting a final product. It is harder to make small changes and personalizations to the charts, but very easy to get quick and intuitive visuals with even large and complex datasets, unlike excel. To match the species colors, I used the teal hex code since that was not an option in the template. However, similarly to excel I had to manually add in the bill_length to the legend area of the chart since this was not an option in the default scatterplot. After research, it does appear that is an option in a "stacked scatter visual from the marketplace", which would be a great option if this was a necessary function for a professional and finalized visual. I would use powerbi again to create a fast and detailed visual of any size dataset that does not require any secific customizations. In the future I know that I will be using this tool for my job and this experiment helped introduce me to the tool and understand how simple it is to use.

![powerbi image](/img/powerbi.png)

---
# Design Achievements
 For most of the visualizations (except powerbi and excel), I chose to cammel case the legend to make it more visually appealing. Throughout each visualization I made sure to replicate the colors, legend, scales, and axis labels as best I could given the constraints of the tool itself. Each visual also included major and minor grid lines, although it is hard to see in the image taken from powerbi due to low resolution screenshot. The opacity of around 0.8 was also preserved in each visual.
