set terminal postscript eps linewidth 2 "Helvetica" 24 size ratio 0.4 enhanced
set xlabel 'Number of Clusters'
set ylabel 'Frames(%)'
set xrange [0:160]
set yrange [0.75:0.85]
set size ratio 0.4
#set xtics 0.1 ,1 ,0.9
#set key inside bottom right
unset key
set output "cluster.eps"
plot 'cluster.txt' using 1:2 with linespoints lt 1 pt 1 lw 2 ps 2
unset output
set term wxt