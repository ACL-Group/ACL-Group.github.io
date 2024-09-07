set terminal postscript eps enhanced font 'Verdana,25'
set output 'figure/hcf1.eps'
set xlabel "Number of Corrections"
set ylabel "Accuracy"
set title "Human Correction (ECG1)"
set key right bottom
set xrange [0:16]
set xtics 0,5,15
plot "data1.dat" using 1:2 w lp ps 2 title "Most Frequent", "data1.dat" using 1:3 w lp ps 2 title "Random"

set terminal postscript eps enhanced font 'Verdana,25'
set output 'figure/hcf2.eps'
set xlabel "Number of Corrections"
set ylabel "Accuracy"
set title "Human Correction (ECG2)"
set xrange [0:16]
set xtics 0,5,15
plot "data2.dat" using 1:2 w lp ps 2 title "Most Frequent", "data2.dat" using 1:3 w lp ps 2 title "Random"

set terminal postscript eps enhanced font 'Verdana,25'
set output 'figure/hcf3.eps'
set xlabel "Number of Corrections"
set ylabel "Accuracy"
set title "Human Correction (ECG3)"
set xrange [0:16]
set xtics 0,5,15
plot "data3.dat" using 1:2 w lp ps 2 title "Most Frequent", "data3.dat" using 1:3 w lp ps 2 title "Random"

set terminal postscript eps enhanced font 'Verdana,20'
set output 'figure/hcf4.eps'
set xlabel "Number of Corrections"
set ylabel "Accuracy"
set title "Human Correction (ECG4)"
set xrange [0:16]
set xtics 0,5,15
plot "data4.dat" using 1:2 w lp ps 2 title "Most Frequent", "data4.dat" using 1:3 w lp ps 2 title "Random"
