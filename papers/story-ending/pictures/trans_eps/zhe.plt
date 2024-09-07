#set termoption font 'Helvetica,20'
set term postscript eps 'Helvetica' 20
set output "../../trend.eps"
set xlabel "Percentage of Data(%)" 
set ylabel "Test Accuracy(%)" 
set title ""
set xrange [0:110]
set yrange [60:71]
set xtics 0,10,100
set ytics 50,2,80
set xtics 
set ytics 
set key 
set key bottom right width 1.5 height 2
plot "acc.dat" u 1:4 w lp pt 5 lw 4 title "SKBC+Simp+CE","acc.dat" u 1:5 w lp pt 7 lw 4 title "SKBC+Simp","acc.dat" u 1:3 w lp pt 3 lw 4 title "SKBC"
