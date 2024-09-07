set terminal postscript eps linewidth 2 "Helvetica" 24 enhanced
set xlabel '{/Symbol \153}'
set ylabel "Recall"
set xrange [0.1:0.9]
set yrange [0:0.03]
#set xtics 0.1 ,1 ,0.9
set output "kappa_all_recall.eps"
plot "kappa_all_recall.dat" using 1:2 w lp pt 1 title columnheader(1), '' using 1:3 w lp pt 2 title columnheader(2)
unset output
set term wxt