set terminal postscript eps color lw 2 solid
set output "exp.eps"
set size 1.0,1.0
set origin 0,0

set multiplot layout 2,2 rowsfirst

set size 0.5,0.5
set origin 0,0.5
set xrange [0.25:0.55]  
set xtic 0.05                                               
set yrange [0.4:1]                                                 
set xlabel "Threshold"                                              
set ylabel "Precision"
set title "Offline Precision"
plot "result.txt" using 1:2 title 'Bi-LSTM-Net' w lp lc 2 lw 1 pt 5 ps 1, "result.txt" using 1:3 title 'Feature-Enriched-Net' w lp lc 7 lw 1 pt 7 ps 1

set size 0.5,0.5
set origin 0.5,0.5
set xrange [0.25:0.55]  
set xtic 0.05                                               
set yrange [0.4:1]                                                 
set xlabel "Threshold"                                              
set ylabel "Recall"
set title "Offline Recall"
plot "result.txt" using 1:4 title 'Bi-LSTM-Net' w lp lc 2 lw 1 pt 5 ps 1, "result.txt" using 1:5 title 'Feature-Enriched-Net' w lp lc 7 lw 1 pt 7 ps 1

set size 0.5,0.5
set origin 0,0
set xrange [0.25:0.55]  
set xtic 0.05                                               
set yrange [0.4:1]                                                 
set xlabel "Threshold"                                              
set ylabel "F-1"
set title "Offline F-1"
plot "result.txt" using 1:6 title 'Bi-LSTM-Net' w lp lc 2 lw 1 pt 5 ps 1, "result.txt" using 1:7 title 'Feature-Enriched-Net' w lp lc 7 lw 1 pt 7 ps 1

set size 0.5,0.5
set origin 0.5,0
set xrange [1:7]  
set xtic 1                                               
set yrange [0:5]
set ytic 0.5
set xlabel "Date in November"                                              
set ylabel "%"
set title "Online A/B Testing"
plot "gmv.txt" using 1:2 title 'Sales Volume' w lp lc 2 lw 1 pt 5 ps 1, "gmv.txt" using 1:3 title 'Turnover Conversion Rate' w lp lc 7 lw 1 pt 7 ps 1

unset multiplot

set output
