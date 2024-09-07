set terminal postscript eps linewidth 2 "Helvetica" 24 enhanced
set style data histogram
set xlabel 'The Deviation'
set ylabel "Number of Verbs"
#set ytics 0,1,7.5
set yrange[0:7.5]
set xtics ("0" 0, "0.01" 1, "0.02" 2, "0.03" 3, "0.04" 4, "0.05" 5)
unset key
set output "try.eps"
plot 'try.txt' using 2
unset output
set term wxt