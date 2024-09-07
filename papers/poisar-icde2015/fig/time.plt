set terminal postscript eps linewidth 2 "Helvetica" 24
set xlabel "# POIs (in thousands)"
set ylabel "Time Cost Per User (ms.)"
#set logscale y
#unset title
#unset key
set xrange [0.8:8]
set xtics 0.8, 0.8 , 8
set yrange [0:40]
set output "time_sg.eps"
plot "time_sg.dat" using 1:1 w lp lc 0 lw 2 pt 3 ps 2 title "B&B",'' using 1:4 w lp lc 0 lw 2 pt 5 ps 2 title "Threshold",'' using 1:2 w lp lc 0 lw 2 pt 2 ps 2 title "Brute-force"
unset output
set term wxt