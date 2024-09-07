set terminal postscript eps color lw 2 solid
set output "exp.eps"
set size 1.0,0.5
set origin 0,0

set multiplot layout 1,2 rowsfirst

set size 0.5,0.5
set origin 0,0
set xrange [0.25:0.55]  
set xtic 0.05                                               
set yrange [0.4:1]                                                 
set xlabel "Threshold"                                              
set ylabel "Precision"
set title "Precision"
plot "result.txt" using 1:2 title 'Bi-LSTM-Net' w lp lc 2 lw 1 pt 5 ps 1, "result.txt" using 1:3 title 'Wide&Deep-Net' w lp lc 7 lw 1 pt 7 ps 1

set size 0.5,0.5
set origin 0.5,0
set xrange [0.25:0.55]  
set xtic 0.05                                               
set yrange [0.4:1]                                                 
set xlabel "Threshold"                                              
set ylabel "Recall"
set title "Recall"
plot "result.txt" using 1:4 title 'Bi-LSTM-Net' w lp lc 2 lw 1 pt 5 ps 1, "result.txt" using 1:5 title 'Wide&Deep-Net' w lp lc 7 lw 1 pt 7 ps 1

#set size 0.5,0.5
#set origin 1,0
#set xrange [0.25:0.55]  
#set xtic 0.05                                               
#set yrange [0.4:1]                                                 
#set xlabel "Threshold"                                              
#set ylabel "F-1"
#set title "F-1"
#plot "result.txt" using 1:6 title 'Bi-LSTM-Net' w lp lc 2 lw 1 pt 5 ps 1, "result.txt" using 1:7 title 'Wide&Deep-Net' w lp lc 7 lw 1 pt 7 ps 1

unset multiplot

set output
