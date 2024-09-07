set terminal postscript eps linewidth 2 "Helvetica" 24
#set pm3d
set xlabel " Avg. Concept Size"
set ylabel "k"
set zlabel "Pruning Ratio"
set zlabel rotate by 90
unset xtics
unset ytics
set zrange [0:1]
set xyplane 0.1
set hidden3d
set view 45,230
#set view 0,0 
unset key
set output "complexity_data.eps"
splot "complexity_data.txt" using 2:1:3 with lines
unset output
set term wxt