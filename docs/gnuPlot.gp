set datafile separator ","
set terminal pngcairo size 900, 700
set output "gnuPlot.png"
set xlabel "Flipper Length (mm)"
set ylabel "Body Mass (g)"
set xrange [170:240]
set yrange [2500:6500]
set key outside right
set style fill solid 0.8 border -1

size(bl) = bl/10.0

plot \
    "penglings.csv" using \
        6:7:(size($4)) \
        every ::1 \
        with points pt 7 ps variable lc rgb "#1f77b4" \
        title "Adelie" \
        if (stringcolumn(2) eq "Adelie"), \
    \
    "penglings.csv" using \
        6:7:(size($4)) \
        every ::1 \
        with points pt 7 ps variable lc rgb "#ff7f0e" \
        title "Chinstrap" \
        if (stringcolumn(2) eq "Chinstrap"), \
    \
    "penglings.csv" using \
        6:7:(size($4)) \
        every ::1 \
        with points pt 7 ps variable lc rgb "#2ca02c" \
        title "Gentoo" \
        if (stringcolumn(2) eq "Gentoo")