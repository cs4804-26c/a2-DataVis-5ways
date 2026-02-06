% found documentation here : https://www.mathworks.com/help/matlab/ref/readtable.html 
data = readtable("https://raw.githubusercontent.com/hsmith1212/a2-DataVis-5ways-has/refs/heads/main/penglings.csv");


%co pilot told me to add this line, because originally I just put species
%as the color variable, but that didn't work because data was reading
%species as seperate strings, not as a category column
data.species = categorical(data.species);



% decided to split instead
adelie = data(data.species == 'Adelie', :);
gentoo = data(data.species == 'Gentoo', :);
chinstrap = data(data.species == 'Chinstrap', :);

t = tiledlayout(1,1);
nexttile
b1 = bubblechart(adelie,'flipper_length_mm','body_mass_g','bill_length_mm')
hold on
b2 = bubblechart(gentoo,'flipper_length_mm','body_mass_g','bill_length_mm')
b3 = bubblechart(chinstrap,'flipper_length_mm','body_mass_g','bill_length_mm')

% found in this documentation: https://www.mathworks.com/help/matlab/creating_plots/change-tick-marks-and-tick-labels-of-graph-1.html
xticks([170 180 190 200 210 220 230])
yticks([3000 4000 5000 6000])

% referenced https://www.mathworks.com/help/matlab/creating_plots/add-title-axis-labels-and-legend-to-graph.html
xlabel('Bill Length (mm)')
ylabel('Body Mass (g)')

% referenced https://www.mathworks.com/matlabcentral/answers/161664-how-do-i-set-a-background-color-in-plots
set(gca,'color', [0.8 0.8 0.8]);

% references for grid lines: https://www.mathworks.com/help/matlab/ref/grid.html
grid on
grid minor
% looked at attributes for syling here https://www.mathworks.com/help/matlab/ref/matlab.graphics.axis.axes-properties.html#budumk7_sep_shared-GridLineStyle

set(gca, 'GridColor', [1 1 1], ...        
         'GridAlpha', 1.0, ...            
         'GridLineStyle', '-', ...
         'LineWidth', 2.0);   
set(gca, 'MinorGridColor', [1 1 1], ...   % white
         'MinorGridAlpha', 0.5, ...       % lighter
         'MinorGridLineStyle', '-', ...
         'MinorGridLineWidth', 0.75);     % thinner minor lines




% googled "{color} matlab triplet" and used answer from google AI
%fill
b1.MarkerFaceColor = [1.0 0.5 0.0]; % orange
b2.MarkerFaceColor = [0.0 0.5 0.5]; % blue
b3.MarkerFaceColor = [0.5 0.0 0.5]; % purple
%outline
b1.MarkerEdgeColor = [1.0 0.5 0.0];
b2.MarkerEdgeColor = [0.0 0.5 0.5];
b3.MarkerEdgeColor = [0.5 0.0 0.5];


% learned to change bubble sizes here: https://www.mathworks.com/help/matlab/ref/bubblesize.html
bubblesize([3,17])

%bubble legend. found attributes here:
%https://www.mathworks.com/help/matlab/ref/bubblelegend.html#d126e149438 
blgd = bubblelegend('bill\_length\_mm', ...
    'Location','eastoutside', ...
    'NumBubbles', 2, ...
    'BubbleSizeOrder','ascending');

%color legend
lgd = legend('Adelie','Gentoo','Chinstrap');

%using the tiles to lay it out
lgd.Layout.Tile = 'east';
blgd.Layout.Tile = 'east';

