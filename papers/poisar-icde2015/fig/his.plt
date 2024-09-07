set terminal postscript eps linewidth 2 "Helvetica" 24
set xlabel "# check-ins at same location"
set ylabel "# user-location pairs(log scale)"
set logscale y
unset title
unset key
set xrange [1:19]
set xtics 1 ,2 ,19
set output "evidence_log.eps"
plot "histogram_umn.dat" w lp lc 0 lw 2 pt 0 ps 1
unset output
set term wxt