data = readtable('penglings.csv');
data = data(:, {'body_mass_g', 'flipper_length_mm', 'bill_length_mm', 'species'});

x = data.flipper_length_mm;
y = data.body_mass_g;
bubbleSize = data.bill_length_mm;

species = categorical(data.species);
valid = ~isnan(x) & ~isnan(y) & ~isnan(bubbleSize) & ~isundefined(species);

s = species(valid);
colors = zeros(numel(s), 3);
for i = 1:numel(s)
    if (species(i) == "Adelie")
        colors(i, :) = [1 0.5 0.2];
    elseif (species(i) == "Chinstrap")
        colors(i, :) = [0.4 0.2 0.6];
    else
        colors(i, :) = [0.05 0.6 0.6];
    end
end

figure
scatter(x(valid), y(valid), (bubbleSize(valid) - 40) * 8 + 170, ...
    colors, 'filled', 'MarkerFaceAlpha', 0.8);
xlabel('Flipper Length (mm)');
ylabel('Bill Length (mm)');

legend('Location', 'best');

s40 = 170; s50 = 250;

hold on
hAdelie = scatter(nan, nan, 70, [1 0.5 0.2], 'filled');
hChinstrap = scatter(nan, nan, 70, [0.4 0.2 0.6], 'filled');
hGentoo = scatter(nan, nan, 70, [0.05 0.6 0.6], 'filled');

legend([hAdelie hChinstrap hGentoo], ...
    {'Adelie', 'Chinstrap', 'Gentoo'}, 'Location', 'best');

grid on