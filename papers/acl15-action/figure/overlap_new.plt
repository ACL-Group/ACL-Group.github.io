set terminal postscript eps linewidth 2 "Helvetica" 24 enhanced
set xlabel 'Number of Concepts(k)'
set ylabel "Overlap"
set xrange [4:11]
set yrange [0:0.5]
#set xtics 0.1 ,1 ,0.9
#set key inside bottom right
set output "overlap_new.eps"
plot 'overlap_new.txt' using 1:2 title 'AC(Subj)' with linespoints lt 1 pt 1 lw 2 ps 2, '' using 1:3 title 'AC(Obj)' with linespoints lt 1 pt 2 lw 2 ps 2, '' using 1:4 title 'AC(Triplet)' with linespoints lt 1 pt 3 lw 2 ps 2, '' using 1:5 title 'SP(Subj)' with linespoints lt 2 pt 1 lw 2 ps 2, '' using 1:6 title 'SP(Obj)' with linespoints lt 2 pt 2 lw 2 ps 2, '' using 1:7 title 'SP(Triplet)' with linespoints lt 2 pt 3 lw 2 ps 2, 
unset output
set term wxt
