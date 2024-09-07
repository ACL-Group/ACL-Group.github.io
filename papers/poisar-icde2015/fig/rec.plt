set terminal postscript eps linewidth 2 "Helvetica" 24
set style data histogram
set key left
set yrange [0:0.08]
set output "user_map.eps"
plot "user_map.dat" using 2:xticlabels(1) title columnheader(2) fs pattern 1, '' using 3:xticlabels(1) title columnheader(3) fs pattern 6, '' using 4:xticlabels(1) title columnheader(4) fs pattern 3
unset output
set term wxt