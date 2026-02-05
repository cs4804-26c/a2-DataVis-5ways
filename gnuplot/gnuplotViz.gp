set terminal pngcairo size 800,600 enhanced font 'Segoe UI,12'
set output 'penguin_chart.png'

set datafile separator ","
set datafile missing "NA"

set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb "#EBEBEB" behind
set border 0
set grid front lc rgb "white" lw 1.5

set xrange [170:235]
set yrange [2500:6500]
set xtics nomirror scale 0
set ytics nomirror scale 0

set xlabel "Flipper Length (mm)" font ",14" offset 0,-1
set ylabel "Body Mass (g)" font ",14" offset -1,0
set title "Penguin Size Comparison" font ",16"

set key outside right top
set key box lc rgb "white" 
set key spacing 1.5
set key textcolor rgb "black"

strip(s) = (s[1:1] eq '"' ? s[2:strlen(s)-1] : s)

plot \
     NaN title "bill length mm" with points pt 0 lc rgb "black", \
     NaN title "40" with points pt 7 ps 1.5 lc rgb "#666666", \
     NaN title "50" with points pt 7 ps 2.5 lc rgb "#666666", \
     NaN title " " with points pt 0, \
     NaN title "species" with points pt 0 lc rgb "black", \
     \
     'penglings.csv' every ::1 using (strip(strcol(2)) eq "Adelie" ? $6 : 1/0):7:($4/25.0) \
     with circles lc rgb "#E28A37" fs solid 0.8 title "Adelie", \
     \
     'penglings.csv' every ::1 using (strip(strcol(2)) eq "Chinstrap" ? $6 : 1/0):7:($4/25.0) \
     with circles lc rgb "#AF58BA" fs solid 0.8 title "Chinstrap", \
     \
     'penglings.csv' every ::1 using (strip(strcol(2)) eq "Gentoo" ? $6 : 1/0):7:($4/25.0) \
     with circles lc rgb "#008080" fs solid 0.8 title "Gentoo"