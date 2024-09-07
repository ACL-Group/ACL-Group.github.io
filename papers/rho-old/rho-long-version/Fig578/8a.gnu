set output "buffersizeavg.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25' size 6,4 lw 2
set key top right vertical maxrows 2
#set boxwidth 1 absolute
set style fill solid border -1
set style data lp
#set ytics nomirror
set xrange [3.5:6.0] 
set yrange [0.0:1.0] 
set xlabel "b_{max}(*10^{6})"
set ylabel "Info Loss"
plot '8a.dat' using 1:2  title "Dist" with lp ps 2,\
'8a.dat' using 1:3 title "Mine" with lp ps 2
