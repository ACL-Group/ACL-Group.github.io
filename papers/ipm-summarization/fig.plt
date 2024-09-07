set terminal postscript eps color lw 2 solid
set output "repeat.eps"
set size 1.1,1.1
set origin 0,0
set key font ",25"
set xtics font ",25"
set ytics font ",22"
set xlabel font ",25"
set ylabel font ",25"
set title font ",36"

set yrange [0:20]      
set ytic 5                                          
set ytics ('0'0, '5'5, '10'10, '20'15, '40'20)
set xtics ('1-gram'1, '2-gram'2, '3-gram'3, '4-gram'4, 'sent'5)
#set xlabel "n-gram"                                           
set ylabel "Repeatedness Score"
set title ""
plot "fig.txt" using 1:2 title 'Gold' w lp lc 7 lw 2 pt 5 ps 2, "fig.txt" using 1:3 title 'ATTF' w lp lc 2 lw 2 pt 7 ps 2, "fig.txt" using 1:4 title 'TRI*' w lp lc 3 lw 2 pt 3 ps 2, "fig.txt" using 1:5 title 'SBD*' w lp lc 4 lw 2 pt 5 ps 2, "fig.txt" using 1:6 title 'ATTF+TRI*' w lp lc 6 lw 2 pt 8 ps 2, "fig.txt" using 1:7 title 'ATTF+SBD*' w lp lc 5 lw 2 pt 6 ps 2

set output
