set output "scaletime.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25' size 6,4 lw 2
set key top right vertical maxrows 2
#set boxwidth 1 absolute
set style fill solid border -1
set style data lp
#set ytics nomirror
set xrange [0:6] noreverse nowriteback
set yrange [0:120] noreverse nowriteback
set xtics ("1/5" 1, "2/5" 2, "3/5" 3, "4/5" 4, "1" 5)
set xlabel "Fraction of Input"
set ylabel "Time(seconds)"
plot '5a.dat' using 1:2  title "Dist" with lp ps 2,\
'5a.dat' using 1:3 title "Mine" with lp ps 2
