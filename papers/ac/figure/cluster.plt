set terminal postscript eps linewidth 2 "Helvetica" 24 enhanced
set xlabel 'm'
set ylabel 'RI'
set xrange [1.2:1.5]
set yrange [0.83:0.89]
#set size ratio 0.4
#set xtics 0.1 ,1 ,0.9
set key inside top right
set output "cluster.eps"
plot 'cluster.txt' using 1:2 title 'Action' with linespoints lt 1 pt 1 lw 3 ps 3, '' using 1:3 title 'SP' with linespoints lt 3 pt 2 lw 3 ps 3
unset output
set term wxt