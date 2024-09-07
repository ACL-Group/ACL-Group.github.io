set output "exp_partition_strategy.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25' size 6,4 lw 2
set key left box
set boxwidth 1 absolute
set style fill solid border -1
set style data histogram
set style histogram cluster gap 1
set ytics nomirror
set y2tics nomirror
set xtics ("InferSpark" 0, "2D" 1, "RVC" 2, "CRVC" 3, "1D" 4)
# set style line 1 lt 1 lw 2 pt 7 ps 1.5
# set style line 2 lt 2 lw 2 pt 8 ps 1.5
set xlabel "partition strategy"
set ylabel "Total running time (second)"
set y2label "EdgeRDD size (GB)"
plot 'partition_strategy_time.dat' using 2  axes x1y1 title "time" fs pattern 0 lt -1,\
'partition_strategy_edgesize.dat' using 2 axes x1y2 title "EdgeRDD size" fs pattern 3 lt -1

