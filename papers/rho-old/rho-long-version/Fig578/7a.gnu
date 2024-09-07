set output "timebond_avg.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25' size 6,4 lw 2
set key top right vertical maxrows 2
#set boxwidth 1 absolute
set style fill solid border -1
set style data lp
#set ytics nomirror
set xrange [0:1000] noreverse nowriteback
set yrange [0.0:1.0] noreverse nowriteback
set xlabel "t_{max}(seconds)"
set ylabel "Info Loss"
plot '7a.dat' using 1:2  title "Dist" with lp ps 2,\
'7a.dat' using 1:3 title "Mine" with lp ps 2
