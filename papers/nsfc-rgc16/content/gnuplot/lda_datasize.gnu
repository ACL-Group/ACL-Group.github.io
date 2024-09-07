set output "exp_lda_datasize.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25'

set style line 1 lt 1 lw 2 pt 3 ps 3
set style line 2 lt 1 lw 2 pt 4 ps 3
set style line 3 lt 1 lw 2 pt 7 ps 3
set key box  bottom right
set xlabel "number of words ({/Symbol \264}10^6)"
set ylabel "Total running time (second)"
plot 'lda_datasize.dat' using ($1/1e6):2 with linespoints ls 1 title "LDA 96 topics",\
'dcmlda_datasize.dat' using ($1/1e6):2 with linespoints ls 2 title "DCMLDA 10 topics",\
'slda_datasize.dat' using ($1/1e6):2 w lp ls 3 title "SLDA 96 topics"

