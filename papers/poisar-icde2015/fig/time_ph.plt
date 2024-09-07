set terminal postscript eps linewidth 2 "Helvetica" 24
set xlabel "# POIs (in thousands)"
set ylabel "Time Cost Per User (ms.)"
#set logscale y
#unset title
#unset key
set xrange [1:10]
set xtics 1, 1 , 10
set yrange [0:100]
set output "time_ph.eps"
plot "time_ph.dat" using 1:2 w lp lc 0 lw 2 pt 3 ps 2 title "B&B",'' using 1:4 w lp lc 0 lw 2 pt 5 ps 2 title "Threshold",'' using 1:3 w lp lc 0 lw 2 pt 2 ps 2 title "Brute-force"
unset output
set term wxt