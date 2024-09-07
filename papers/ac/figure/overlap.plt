set terminal postscript eps linewidth 2 "Helvetica" 24 enhanced
set xlabel 'Number of Concepts(k)'
set ylabel "Overlap"
set xrange [0:11]
#set yrange [0:0.25]
#set xtics 0.1 ,1 ,0.9
#set key inside bottom right
set output "overlap.eps"
plot 'overlap.txt' using 1:2 title 'Action(Web)' with linespoints lt 1 pt 1 lw 2 ps 2, '' using 1:3 title 'SP(Web)' with linespoints lt 3 pt 2 lw 2 ps 2
unset output
set term wxt