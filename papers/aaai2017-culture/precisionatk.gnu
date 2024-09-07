#!/usr/bin/gnuplot

reset

# svg
#set terminal svg size 350,262 fname 'Verdana, Helvetica, Arial, sans-serif' fsize '10'
#set output 'plot.svg'

# epslatex
set terminal epslatex size 3.5,2.62 color colortext font ',9'
set output 'precisionatk.tex'

# color definitions
# set border linewidth 1.5
set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 2 ps 1 # --- blue
set style line 2 lc rgb '#dd181f' lt 1 lw 2 pt 5 ps 1 # --- red
set style line 3 lc rgb '#00ff00' lt 1 lw 2 pt 8 ps 1 # --- green
set style line 4 lc rgb '#000000' dashtype 2 lw 2 

set xlabel 'top $k$'
set ylabel "precision at $k$"

# set ytics 1
# set tics scale 0.75

set xrange [0:190]
set yrange [0.4:0.85]

plot 0.45646438 ls 4 t 'ER', \
     'precisionatk.dat' index 0 with linespoints ls 1 t 'PR', \
     ''         index 1 with linespoints ls 2 t 'LT', \
     ''         index 2 with linespoints ls 3 t 'TS'
