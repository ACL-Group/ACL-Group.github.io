set xlabel "样本规模大小"
set ylabel "性能"
set title "我国主要海域监测情况"
set xrange [0.5:4.5]
set yrange [:]
set datafile separator " "
set output 'roc.pdf'
plot "test.dat" using 1:2 w lp pt 5
