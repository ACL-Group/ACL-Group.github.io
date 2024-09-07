set output "exp_clustersize.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25'

set style line 1 lt 1 lw 2 pt 3 ps 3
set style line 2 lt 1 lw 2 pt 4 ps 3
set style line 3 lt 1 lw 2 pt 7 ps 3
set key top right
set xlabel "number of nodes"
set ylabel "Total running time (second)"
set xtics autofreq nomirror
set xrange [22:50]
plot 'clustersize.dat' using 1:2:xtic(1) with linespoints ls 2 t "LDA",\
'clustersize.dat' using 1:3:xtic(1) with linespoints ls 3 t "DCMLDA",\
'clustersize.dat' using 1:4:xtic(1) with linespoints ls 1 t "SLDA"

