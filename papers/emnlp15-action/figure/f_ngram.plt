set terminal postscript eps linewidth 2 "Helvetica" 24 enhanced
set xlabel 'Number of Concepts(k)'
set ylabel "F1"
set xrange [0:11]
set yrange [0.35:0.9]
#set xtics 0.1 ,1 ,0.9
#set key inside top right
set key inside bottom right
set output "f_ngram.eps"
plot 'f_ngram.txt' using 1:2 title 'AC(MI)' with linespoints lt 1 pt 1 lw 2 ps 2, '' using 1:4 title 'AC(TF-IDF)' with linespoints lt 3 pt 3 lw 2 ps 2, '' using 1:3 title 'SP' with linespoints lt 2 pt 2 lw 2 ps 2
unset output
set term wxt