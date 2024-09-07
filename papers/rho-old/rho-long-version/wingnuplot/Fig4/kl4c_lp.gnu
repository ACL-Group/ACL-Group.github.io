set output "KL.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25' size 6,4 lw 2
set key top right vertical maxrows 4
#set boxwidth 1 absolute
set style fill solid border -1
set style data histogram
set style histogram cluster gap 2
set logscale y
set ytics nomirror
set xrange [0.0:1.0]
set yrange [0.001:10]
set format y "10^{%L}"
# set style line 1 lt 1 lw 2 pt 7 ps 1.5
# set style line 2 lt 2 lw 2 pt 8 ps 1.5
set xlabel "Rho"
set ylabel "Symmetric K-L Divergence(Log)"
plot 'kl4c.dat' using 1:2  title "POS Dist" with lp ps 2,\
'kl4c.dat' using 1:3 title "POS Mine" with lp ps 2,\
'kl4c.dat' using 1:4 title "WV Dist" with lp ps 2,\
'kl4c.dat' using 1:5 title "WV Mine" with lp ps 2,\
'kl4c.dat' using 1:6 title "Retail Dist" with lp ps 2,\
'kl4c.dat' using 1:7 title "Retail Mine" with lp ps 2,\
'kl4c.dat' using 1:8 title "Syn Dist" with lp ps 2,\
'kl4c.dat' using 1:9 title "Syn Mine" with lp ps 2
