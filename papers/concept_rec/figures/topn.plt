set terminal postscript eps color lw 2 solid
set output "topn.eps"
set size 2.0,1.0
set origin 0,0
set key font ",28"
set tics font ",30"
set xlabel font ",30"
set ylabel font ",30"
set title font ",36"


set multiplot layout 2,1 rowsfirst

set size 1.0,1.0
set origin 0,0         
set yrange [0:0.7]      
set ytic 0.2                                          
set xtics ('1'1, '5'2, '10'3, '20'4, '50'5, '100'6)
set xlabel "N"                                           
set ylabel "HR"
set title "HR\\@N"
plot "recall.txt" using 1:2 title 'CptInfer' w lp lc 7 lw 2 pt 5 ps 2, "recall.txt" using 1:3 title 'BPR' w lp lc 2 lw 2 pt 7 ps 2, "recall.txt" using 1:4 title 'MCRec' w lp lc 3 lw 2 pt 3 ps 2, "recall.txt" using 1:5 title 'Wide\&Deep' w lp lc 4 lw 2 pt 5 ps 2, "recall.txt" using 1:6 title 'KPRN' w lp lc 5 lw 2 pt 6 ps 2



set size 1.0,1.0
set origin 1,0
set yrange [0:0.15]      
set ytic 0.05                                            
set xtics ('1'1, '5'2, '10'3, '20'4, '50'5, '100'6) 
set xlabel "N"                                           
set ylabel "NDCG"
set title "NDCG\\@N"
plot "precision.txt" using 1:2 title 'CptInfer' w lp lc 7 lw 2 pt 5 ps 2, "precision.txt" using 1:3 title 'BPR' w lp lc 2 lw 2 pt 7 ps 2, "precision.txt" using 1:4 title 'MCRec' w lp lc 3 lw 2 pt 3 ps 2, "precision.txt" using 1:5 title 'Wide\&Deep' w lp lc 4 lw 2 pt 5 ps 2, "precision.txt" using 1:6 title 'KPRN' w lp lc 5 lw 2 pt 6 ps 2

unset multiplot

set output
