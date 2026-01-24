penglings = readtable('../penglings.csv');

valid = ~isnan(penglings.flipper_length_mm) & ...
        ~isnan(penglings.body_mass_g) & ...
        ~isnan(penglings.bill_length_mm);

species = categorical(penglings.species(valid));
x = penglings.flipper_length_mm(valid);
y = penglings.body_mass_g(valid);
s = rescale(penglings.bill_length_mm(valid), 20, 200);

figure
hold on

cats = categories(species);
colors = lines(numel(cats));

for i = 1:numel(cats)
    idx = species == cats{i};
    scatter(x(idx), y(idx), s(idx), ...
            'filled', ...
            'MarkerFaceColor', colors(i,:));
end

hold off
legend(cats, 'Location', 'best')
xlabel('Flipper Length (mm)')
ylabel('Body Mass (g)')
grid on
