set terminal postscript eps linewidth 2 "Helvetica" 24
set style data histogram
set key left
set yrange [0:0.05]
set output "user_map.eps"
plot "user_map.dat" using 2:xticlabels(1) title columnheader(2) fs pattern 1, '' using 3:xticlabels(1) title columnheader(3) fs pattern 2, '' using 4:xticlabels(1) title columnheader(4) fs pattern 7, '' using 5:xticlabels(1) title columnheader(5) fs pattern 4,'' using 6:xticlabels(1) title columnheader(6) fs pattern 5,'' using 7:xticlabels(1) title columnheader(7) fs pattern 6,'' using 8:xticlabels(1) title columnheader(8) fs pattern 3
unset output
set term wxt